# Copyright 2018 The Cirq Developers
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

"""Cirq is a framework for creating, editing, and invoking quantum circuits."""

from cirq import _import

# A module can only depend on modules imported earlier in this list of modules
# at import time.  Pytest will fail otherwise (enforced by
# dev_tools/import_test.py).
# Begin dependency order list of sub-modules.
from cirq import (
    # Low level
    _version,
    _doc,
    type_workarounds,
)

with _import.delay_import('cirq.protocols'):
    from cirq import (
        # Core
        protocols,
        value,
        linalg,
        qis,
        ops,
        devices,
        study,
    )
from cirq import (
    # Core
    circuits,
    # Optimize and run
    optimizers,
    work,
    sim,
    vis,
    # Hardware specific
    ion,
    neutral_atoms,
    interop,
    # Applications
    experiments,
    # Extra (nothing should depend on these)
    testing,
)

# End dependency order list of sub-modules

from cirq._version import (
    __version__,
)

# Flattened sub-modules.

from cirq.circuits import (
    AbstractCircuit,
    Alignment,
    Circuit,
    CircuitDag,
    CircuitOperation,
    FrozenCircuit,
    InsertStrategy,
    Moment,
    PointOptimizationSummary,
    PointOptimizer,
    QasmOutput,
    QuilOutput,
    TextDiagramDrawer,
    Unique,
)

from cirq.devices import (
    ConstantQubitNoiseModel,
    Device,
    DeviceMetadata,
    GridDeviceMetadata,
    GridQid,
    GridQubit,
    LineQid,
    LineQubit,
    NO_NOISE,
    NOISE_MODEL_LIKE,
    NoiseModel,
    NoiseModelFromNoiseProperties,
    NoiseProperties,
    OpIdentifier,
    SymmetricalQidPair,
    UNCONSTRAINED_DEVICE,
    NamedTopology,
    draw_gridlike,
    LineTopology,
    TiltedSquareLattice,
    get_placements,
    draw_placements,
)

from cirq.experiments import (
    TensoredConfusionMatrices,
    estimate_parallel_single_qubit_readout_errors,
    estimate_single_qubit_readout_errors,
    hog_score_xeb_fidelity_from_probabilities,
    least_squares_xeb_fidelity_from_expectations,
    least_squares_xeb_fidelity_from_probabilities,
    linear_xeb_fidelity,
    linear_xeb_fidelity_from_probabilities,
    log_xeb_fidelity,
    log_xeb_fidelity_from_probabilities,
    generate_boixo_2018_supremacy_circuits_v2,
    generate_boixo_2018_supremacy_circuits_v2_bristlecone,
    generate_boixo_2018_supremacy_circuits_v2_grid,
    measure_confusion_matrix,
    xeb_fidelity,
)

from cirq.interop import (
    quirk_json_to_circuit,
    quirk_url_to_circuit,
)

from cirq.linalg import (
    all_near_zero,
    all_near_zero_mod,
    allclose_up_to_global_phase,
    apply_matrix_to_slices,
    axis_angle,
    AxisAngleDecomposition,
    bidiagonalize_real_matrix_pair_with_symmetric_products,
    bidiagonalize_unitary_with_special_orthogonals,
    block_diag,
    CONTROL_TAG,
    deconstruct_single_qubit_matrix_into_angles,
    density_matrix_kronecker_product,
    diagonalize_real_symmetric_and_sorted_diagonal_matrices,
    diagonalize_real_symmetric_matrix,
    dot,
    expand_matrix_in_orthogonal_basis,
    hilbert_schmidt_inner_product,
    is_cptp,
    is_diagonal,
    is_hermitian,
    is_normal,
    is_orthogonal,
    is_special_orthogonal,
    is_special_unitary,
    is_unitary,
    kak_canonicalize_vector,
    kak_decomposition,
    kak_vector,
    KakDecomposition,
    kron,
    kron_bases,
    kron_factor_4x4_to_2x2s,
    kron_with_controls,
    map_eigenvalues,
    match_global_phase,
    matrix_commutes,
    matrix_from_basis_coefficients,
    num_cnots_required,
    partial_trace,
    partial_trace_of_state_vector_as_mixture,
    PAULI_BASIS,
    scatter_plot_normalized_kak_interaction_coefficients,
    pow_pauli_combination,
    reflection_matrix_pow,
    slice_for_qubits_equal_to,
    state_vector_kronecker_product,
    so4_to_magic_su2s,
    sub_state_vector,
    targeted_conjugate_about,
    targeted_left_multiply,
    to_special,
    unitary_eig,
)

from cirq.ops import (
    amplitude_damp,
    AmplitudeDampingChannel,
    AnyIntegerPowerGateFamily,
    AnyUnitaryGateFamily,
    ArithmeticOperation,
    asymmetric_depolarize,
    AsymmetricDepolarizingChannel,
    BaseDensePauliString,
    bit_flip,
    BitFlipChannel,
    BooleanHamiltonian,
    CCX,
    CCXPowGate,
    CCZ,
    CCZPowGate,
    CCNOT,
    CCNotPowGate,
    ClassicallyControlledOperation,
    CNOT,
    CNotPowGate,
    ControlledGate,
    ControlledOperation,
    cphase,
    CSWAP,
    CSwapGate,
    CX,
    CXPowGate,
    CZ,
    CZPowGate,
    DensePauliString,
    depolarize,
    DepolarizingChannel,
    DiagonalGate,
    EigenGate,
    flatten_op_tree,
    flatten_to_ops,
    flatten_to_ops_or_moments,
    FREDKIN,
    freeze_op_tree,
    FSimGate,
    Gate,
    GateFamily,
    GateOperation,
    Gateset,
    generalized_amplitude_damp,
    GeneralizedAmplitudeDampingChannel,
    givens,
    GlobalPhaseGate,
    GlobalPhaseOperation,
    global_phase_operation,
    H,
    HPowGate,
    I,
    identity_each,
    IdentityGate,
    InterchangeableQubitsGate,
    ISWAP,
    ISwapPowGate,
    KrausChannel,
    LinearCombinationOfGates,
    LinearCombinationOfOperations,
    MatrixGate,
    MixedUnitaryChannel,
    measure,
    measure_each,
    measure_paulistring_terms,
    measure_single_paulistring,
    MeasurementGate,
    MutableDensePauliString,
    MutablePauliString,
    NamedQubit,
    NamedQid,
    OP_TREE,
    Operation,
    ParallelGate,
    ParallelGateFamily,
    parallel_gate_op,
    Pauli,
    PAULI_GATE_LIKE,
    PAULI_STRING_LIKE,
    PauliInteractionGate,
    PauliMeasurementGate,
    PauliString,
    PauliStringGateOperation,
    PauliStringPhasor,
    PauliStringPhasorGate,
    PauliSum,
    PauliSumExponential,
    PauliSumLike,
    PauliTransform,
    phase_damp,
    phase_flip,
    PhaseDampingChannel,
    PhaseGradientGate,
    PhasedFSimGate,
    PhasedISwapPowGate,
    PhasedXPowGate,
    PhasedXZGate,
    PhaseFlipChannel,
    StatePreparationChannel,
    ProjectorString,
    ProjectorSum,
    RandomGateChannel,
    qft,
    Qid,
    QuantumFourierTransformGate,
    QubitOrder,
    QubitOrderOrList,
    QubitPermutationGate,
    reset,
    reset_each,
    ResetChannel,
    riswap,
    Rx,
    Ry,
    Rz,
    rx,
    ry,
    rz,
    S,
    SingleQubitCliffordGate,
    SingleQubitGate,
    SingleQubitPauliStringGateOperation,
    SQRT_ISWAP,
    SQRT_ISWAP_INV,
    SWAP,
    SwapPowGate,
    T,
    TaggedOperation,
    ThreeQubitDiagonalGate,
    TOFFOLI,
    transform_op_tree,
    TwoQubitDiagonalGate,
    VirtualTag,
    wait,
    WaitGate,
    X,
    XPowGate,
    XX,
    XXPowGate,
    Y,
    YPowGate,
    YY,
    YYPowGate,
    Z,
    ZPowGate,
    ZZ,
    ZZPowGate,
)

from cirq.optimizers import (
    AlignLeft,
    AlignRight,
    ConvertToCzAndSingleGates,
    DropEmptyMoments,
    DropNegligible,
    EjectPhasedPaulis,
    EjectZ,
    ExpandComposite,
    merge_single_qubit_gates_into_phased_x_z,
    merge_single_qubit_gates_into_phxz,
    MergeInteractions,
    MergeInteractionsToSqrtIswap,
    MergeSingleQubitGates,
    stratified_circuit,
    SynchronizeTerminalMeasurements,
)

from cirq.transformers import (
    align_left,
    align_right,
    compute_cphase_exponents_for_fsim_decomposition,
    decompose_clifford_tableau_to_operations,
    decompose_cphase_into_two_fsim,
    decompose_multi_controlled_x,
    decompose_multi_controlled_rotation,
    decompose_two_qubit_interaction_into_four_fsim_gates,
    drop_empty_moments,
    drop_negligible_operations,
    eject_phased_paulis,
    eject_z,
    expand_composite,
    is_negligible_turn,
    map_moments,
    map_operations,
    map_operations_and_unroll,
    merge_moments,
    merge_operations,
    prepare_two_qubit_state_using_cz,
    prepare_two_qubit_state_using_sqrt_iswap,
    single_qubit_matrix_to_gates,
    single_qubit_matrix_to_pauli_rotations,
    single_qubit_matrix_to_phased_x_z,
    single_qubit_matrix_to_phxz,
    single_qubit_op_to_framed_phase_form,
    synchronize_terminal_measurements,
    TRANSFORMER,
    TransformerContext,
    TransformerLogger,
    three_qubit_matrix_to_operations,
    transformer,
    two_qubit_matrix_to_diagonal_and_operations,
    two_qubit_matrix_to_operations,
    two_qubit_matrix_to_sqrt_iswap_operations,
    two_qubit_gate_product_tabulation,
    TwoQubitGateTabulation,
    TwoQubitGateTabulationResult,
    unroll_circuit_op,
    unroll_circuit_op_greedy_earliest,
    unroll_circuit_op_greedy_frontier,
)

from cirq.qis import (
    bloch_vector_from_state_vector,
    choi_to_kraus,
    choi_to_superoperator,
    CliffordTableau,
    density_matrix,
    density_matrix_from_state_vector,
    dirac_notation,
    entanglement_fidelity,
    eye_tensor,
    fidelity,
    kraus_to_choi,
    kraus_to_superoperator,
    one_hot,
    operation_to_choi,
    operation_to_superoperator,
    QUANTUM_STATE_LIKE,
    QuantumState,
    quantum_state,
    STATE_VECTOR_LIKE,
    StabilizerState,
    superoperator_to_choi,
    superoperator_to_kraus,
    to_valid_density_matrix,
    to_valid_state_vector,
    validate_density_matrix,
    validate_indices,
    validate_normalized_state_vector,
    validate_qid_shape,
    von_neumann_entropy,
)

from cirq.sim import (
    ActOnArgs,
    ActOnArgsContainer,
    ActOnCliffordTableauArgs,
    ActOnDensityMatrixArgs,
    ActOnStabilizerCHFormArgs,
    ActOnStabilizerArgs,
    ActOnStateVectorArgs,
    StabilizerStateChForm,
    CIRCUIT_LIKE,
    CliffordSimulator,
    CliffordState,
    CliffordSimulatorStepResult,
    CliffordTrialResult,
    DensityMatrixSimulator,
    DensityMatrixSimulatorState,
    DensityMatrixStepResult,
    DensityMatrixTrialResult,
    measure_density_matrix,
    measure_state_vector,
    final_density_matrix,
    final_state_vector,
    OperationTarget,
    sample,
    sample_density_matrix,
    sample_state_vector,
    sample_sweep,
    SimulatesAmplitudes,
    SimulatesExpectationValues,
    SimulatesFinalState,
    SimulatesIntermediateState,
    SimulatesIntermediateStateVector,
    SimulatesSamples,
    SimulationTrialResult,
    SimulationTrialResultBase,
    Simulator,
    SimulatorBase,
    SparseSimulatorStep,
    StabilizerSampler,
    StateVectorMixin,
    StateVectorSimulatorState,
    StateVectorStepResult,
    StateVectorTrialResult,
    StepResult,
    StepResultBase,
)

from cirq.study import (
    dict_to_product_sweep,
    dict_to_zip_sweep,
    ExpressionMap,
    flatten,
    flatten_with_params,
    flatten_with_sweep,
    ResultDict,
    Linspace,
    ListSweep,
    ParamDictType,
    ParamResolver,
    ParamResolverOrSimilarType,
    Points,
    Product,
    Sweep,
    Sweepable,
    to_resolvers,
    to_sweep,
    to_sweeps,
    Result,
    UnitSweep,
    Zip,
)

from cirq.value import (
    ABCMetaImplementAnyOneOf,
    alternative,
    big_endian_bits_to_int,
    big_endian_digits_to_int,
    big_endian_int_to_bits,
    big_endian_int_to_digits,
    canonicalize_half_turns,
    chosen_angle_to_canonical_half_turns,
    chosen_angle_to_half_turns,
    ClassicalDataDictionaryStore,
    ClassicalDataStore,
    ClassicalDataStoreReader,
    Condition,
    Duration,
    DURATION_LIKE,
    GenericMetaImplementAnyOneOf,
    KeyCondition,
    LinearDict,
    MEASUREMENT_KEY_SEPARATOR,
    MeasurementKey,
    MeasurementType,
    PeriodicValue,
    RANDOM_STATE_OR_SEED_LIKE,
    state_vector_to_probabilities,
    SympyCondition,
    Timestamp,
    TParamKey,
    TParamVal,
    validate_probability,
    value_equality,
    KET_PLUS,
    KET_MINUS,
    KET_IMAG,
    KET_MINUS_IMAG,
    KET_ZERO,
    KET_ONE,
    PAULI_STATES,
    ProductState,
)

# pylint: disable=redefined-builtin
from cirq.protocols import (
    act_on,
    apply_channel,
    apply_mixture,
    apply_unitaries,
    apply_unitary,
    ApplyChannelArgs,
    ApplyMixtureArgs,
    ApplyUnitaryArgs,
    approx_eq,
    circuit_diagram_info,
    CircuitDiagramInfo,
    CircuitDiagramInfoArgs,
    cirq_type_from_json,
    commutes,
    control_keys,
    decompose,
    decompose_once,
    decompose_once_with_qubits,
    DEFAULT_RESOLVERS,
    definitely_commutes,
    equal_up_to_global_phase,
    has_kraus,
    has_mixture,
    has_stabilizer_effect,
    has_unitary,
    HasJSONNamespace,
    inverse,
    is_measurement,
    is_parameterized,
    JsonResolver,
    json_cirq_type,
    json_namespace,
    json_serializable_dataclass,
    dataclass_json_dict,
    kraus,
    LabelEntity,
    measurement_key_name,
    measurement_key_obj,
    measurement_key_names,
    measurement_key_objs,
    measurement_keys_touched,
    mixture,
    mul,
    num_qubits,
    parameter_names,
    parameter_symbols,
    pauli_expansion,
    phase_by,
    pow,
    qasm,
    QasmArgs,
    qid_shape,
    quil,
    QuilFormatter,
    read_json_gzip,
    read_json,
    resolve_parameters,
    resolve_parameters_once,
    SerializableByKey,
    SupportsActOn,
    SupportsActOnQubits,
    SupportsApplyChannel,
    SupportsApplyMixture,
    SupportsApproximateEquality,
    SupportsConsistentApplyUnitary,
    SupportsCircuitDiagramInfo,
    SupportsCommutes,
    SupportsControlKey,
    SupportsDecompose,
    SupportsDecomposeWithQubits,
    SupportsEqualUpToGlobalPhase,
    SupportsExplicitHasUnitary,
    SupportsExplicitQidShape,
    SupportsExplicitNumQubits,
    SupportsJSON,
    SupportsKraus,
    SupportsMeasurementKey,
    SupportsMixture,
    SupportsParameterization,
    SupportsPauliExpansion,
    SupportsPhase,
    SupportsQasm,
    SupportsQasmWithArgs,
    SupportsQasmWithArgsAndQubits,
    SupportsTraceDistanceBound,
    SupportsUnitary,
    to_json_gzip,
    to_json,
    obj_to_dict_helper,
    trace_distance_bound,
    trace_distance_from_angle_list,
    unitary,
    validate_mixture,
    with_key_path,
    with_key_path_prefix,
    with_measurement_key_mapping,
    with_rescoped_keys,
)

from cirq.ion import (
    ConvertToIonGates,
    IonDevice,
    ms,
    two_qubit_matrix_to_ion_operations,
)
from cirq.neutral_atoms import (
    ConvertToNeutralAtomGates,
    is_native_neutral_atom_gate,
    is_native_neutral_atom_op,
    NeutralAtomDevice,
)

from cirq.vis import (
    Heatmap,
    TwoQubitInteractionHeatmap,
    get_state_histogram,
    integrated_histogram,
    plot_density_matrix,
    plot_state_histogram,
)

from cirq.work import (
    CircuitSampleJob,
    PauliSumCollector,
    Sampler,
    Collector,
    ZerosSampler,
)

# pylint: enable=redefined-builtin

# Unflattened sub-modules.

from cirq import (
    testing,
)

# Registers cirq-core's public classes for JSON serialization.
# pylint: disable=wrong-import-position
from cirq.protocols.json_serialization import _register_resolver
from cirq.json_resolver_cache import _class_resolver_dictionary


_register_resolver(_class_resolver_dictionary)

# contrib's json resolver cache depends on cirq.DEFAULT_RESOLVER

from cirq import (
    contrib,
)

# deprecate cirq.ops.moment and related attributes

from cirq import _compat

_compat.deprecated_submodule(
    new_module_name='cirq.circuits.moment',
    old_parent='cirq.ops',
    old_child='moment',
    deadline='v0.16',
    create_attribute=True,
)

ops.Moment = Moment  # type: ignore
_compat.deprecate_attributes(
    'cirq.ops',
    {
        'Moment': ('v0.16', 'Use cirq.circuits.Moment instead'),
    },
)

# pylint: enable=wrong-import-position
