# Copyright 2021 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import dataclasses

import cirq
import cirq_google
import pytest
from cirq_google import (
    QuantumExecutable,
    BitstringsMeasurement,
    KeyValueExecutableSpec,
    QuantumExecutableGroup,
)


def test_bitstrings_measurement():
    bs = BitstringsMeasurement(n_repetitions=10_000)
    cirq.testing.assert_equivalent_repr(bs, global_vals={'cirq_google': cirq_google})


def _get_random_circuit(qubits, n_moments=10, op_density=0.8, random_state=52):
    return cirq.testing.random_circuit(
        qubits, n_moments=n_moments, op_density=op_density, random_state=random_state
    )


def _get_example_spec(name='example-program'):
    return KeyValueExecutableSpec.from_dict(
        dict(name=name), executable_family='cirq_google.algo_benchmarks.example'
    )


def test_kv_executable_spec():
    kv1 = KeyValueExecutableSpec.from_dict(
        dict(name='test', idx=5), executable_family='cirq_google.algo_benchmarks.example'
    )
    kv2 = KeyValueExecutableSpec(
        executable_family='cirq_google.algo_benchmarks.example',
        key_value_pairs=(('name', 'test'), ('idx', 5)),
    )
    assert kv1 == kv2
    assert hash(kv1) == hash(kv2)

    with pytest.raises(TypeError, match='unhashable.*'):
        hash(KeyValueExecutableSpec(executable_family='', key_value_pairs=[('name', 'test')]))


def test_kv_repr():
    kv = _get_example_spec()
    cirq.testing.assert_equivalent_repr(kv, global_vals={'cirq_google': cirq_google})


def test_quantum_executable(tmpdir):
    qubits = cirq.LineQubit.range(10)
    exe = QuantumExecutable(
        spec=_get_example_spec(name='example-program'),
        circuit=_get_random_circuit(qubits),
        measurement=BitstringsMeasurement(n_repetitions=10),
    )

    # Check args get turned into immutable fields
    assert isinstance(exe.circuit, cirq.FrozenCircuit)

    assert hash(exe) is not None
    assert hash(dataclasses.astuple(exe)) is not None
    assert hash(dataclasses.astuple(exe)) == exe._hash

    prog2 = QuantumExecutable(
        spec=_get_example_spec(name='example-program'),
        circuit=_get_random_circuit(qubits),
        measurement=BitstringsMeasurement(n_repetitions=10),
    )
    assert exe == prog2
    assert hash(exe) == hash(prog2)

    prog3 = QuantumExecutable(
        spec=_get_example_spec(name='example-program'),
        circuit=_get_random_circuit(qubits),
        measurement=BitstringsMeasurement(n_repetitions=20),  # note: changed n_repetitions
    )
    assert exe != prog3
    assert hash(exe) != hash(prog3)

    with pytest.raises(dataclasses.FrozenInstanceError):
        prog3.measurement.n_repetitions = 10

    cirq.to_json(exe, f'{tmpdir}/exe.json')
    exe_reconstructed = cirq.read_json(f'{tmpdir}/exe.json')
    assert exe == exe_reconstructed

    assert (
        str(exe) == "QuantumExecutable(spec=cirq_google.KeyValueExecutableSpec("
        "executable_family='cirq_google.algo_benchmarks.example', "
        "key_value_pairs=(('name', 'example-program'),)))"
    )
    cirq.testing.assert_equivalent_repr(exe, global_vals={'cirq_google': cirq_google})


def test_quantum_executable_inputs():
    qubits = cirq.LineQubit.range(10)
    spec = _get_example_spec(name='example-program')
    circuit = _get_random_circuit(qubits)
    measurement = BitstringsMeasurement(n_repetitions=10)

    params1 = {'theta': 0.2}
    params2 = cirq.ParamResolver({'theta': 0.2})
    params3 = [('theta', 0.2)]
    params4 = (('theta', 0.2),)
    exes = [
        QuantumExecutable(spec=spec, circuit=circuit, measurement=measurement, params=p)
        for p in [params1, params2, params3, params4]
    ]
    for exe in exes:
        assert exe == exes[0]

    with pytest.raises(ValueError):
        _ = QuantumExecutable(
            spec=spec, circuit=circuit, measurement=measurement, params='theta=0.2'
        )
    with pytest.raises(TypeError):
        _ = QuantumExecutable(spec={'name': 'main'}, circuit=circuit, measurement=measurement)


def _get_quantum_executables():
    qubits = cirq.LineQubit.range(10)
    return [
        QuantumExecutable(
            spec=_get_example_spec(name=f'example-program-{i}'),
            problem_topology=cirq.LineTopology(10),
            circuit=_get_random_circuit(qubits, random_state=i),
            measurement=BitstringsMeasurement(n_repetitions=10),
        )
        for i in range(3)
    ]


def test_quantum_executable_group_to_tuple():
    exes1 = list(_get_quantum_executables())
    exes2 = tuple(_get_quantum_executables())

    eg1 = QuantumExecutableGroup(exes1)
    eg2 = QuantumExecutableGroup(exes2)
    assert hash(eg1) == hash(eg2)
    assert eg1 == eg2


def test_quantum_executable_group_methods():
    exes = _get_quantum_executables()
    eg = QuantumExecutableGroup(exes)

    # pylint: disable=line-too-long
    assert str(eg) == (
        "QuantumExecutableGroup(executables=["
        "QuantumExecutable(spec=cirq_google.KeyValueExecutableSpec(executable_family='cirq_google.algo_benchmarks.example', key_value_pairs=(('name', 'example-program-0'),))), "
        "QuantumExecutable(spec=cirq_google.KeyValueExecutableSpec(executable_family='cirq_google.algo_benchmarks.example', key_value_pairs=(('name', 'example-program-1'),))), ...])"
    )
    # pylint: enable=line-too-long

    assert len(eg) == len(exes), '__len__'
    assert exes == [e for e in eg], '__iter__'


def test_quantum_executable_group_serialization(tmpdir):
    exes = _get_quantum_executables()
    eg = QuantumExecutableGroup(exes)

    cirq.testing.assert_equivalent_repr(eg, global_vals={'cirq_google': cirq_google})

    cirq.to_json(eg, f'{tmpdir}/eg.json')
    eg_reconstructed = cirq.read_json(f'{tmpdir}/eg.json')
    assert eg == eg_reconstructed
