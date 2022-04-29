import re

from pymoo.config import Config


# =========================================================================================================
# Generic
# =========================================================================================================



def get_from_list(l, name, args, kwargs):
    i = None

    for k, e in enumerate(l):
        if e[0] == name:
            i = k
            break

    if i is None:
        for k, e in enumerate(l):
            if re.match(e[0], name):
                i = k
                break

    if i is not None:

        if len(l[i]) == 2:
            name, clazz = l[i]

        elif len(l[i]) == 3:
            name, clazz, default_kwargs = l[i]

            # overwrite the default if provided
            for key, val in kwargs.items():
                default_kwargs[key] = val
            kwargs = default_kwargs

        return clazz(*args, **kwargs)
    else:
        raise Exception("Object '%s' for not found in %s" % (name, [e[0] for e in l]))


# =========================================================================================================
# Algorithms
# =========================================================================================================

def get_algorithm_options():
    from pymoo.algorithms.moo.ctaea import CTAEA
    from pymoo.algorithms.moo.moead import MOEAD
    from pymoo.algorithms.moo.nsga2 import NSGA2
    from pymoo.algorithms.moo.nsga3 import NSGA3
    from pymoo.algorithms.moo.rnsga2 import RNSGA2
    from pymoo.algorithms.moo.rnsga3 import RNSGA3
    from pymoo.algorithms.soo.nonconvex.de import DE
    from pymoo.algorithms.soo.nonconvex.ga import GA
    from pymoo.algorithms.moo.unsga3 import UNSGA3
    from pymoo.algorithms.soo.nonconvex.nelder_mead import NelderMead
    from pymoo.algorithms.soo.nonconvex.cmaes import CMAES
    from pymoo.algorithms.soo.nonconvex.brkga import BRKGA
    from pymoo.algorithms.soo.nonconvex.pattern_search import PatternSearch
    from pymoo.algorithms.soo.nonconvex.pso import PSO

    ALGORITHMS = [
        ("ga", GA),
        ("brkga", BRKGA),
        ("de", DE),
        ("nelder-mead", NelderMead),
        ("pattern-search", PatternSearch),
        ("cmaes", CMAES),
        ("pso", PSO),
        ("nsga2", NSGA2),
        ("rnsga2", RNSGA2),
        ("nsga3", NSGA3),
        ("unsga3", UNSGA3),
        ("rnsga3", RNSGA3),
        ("moead", MOEAD),
        ("ctaea", CTAEA),
    ]

    return ALGORITHMS


def get_algorithm(name, *args, d={}, **kwargs):
    return get_from_list(get_algorithm_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Sampling
# =========================================================================================================

def get_sampling_options():
    from pymoo.operators.sampling.lhs import LatinHypercubeSampling
    from pymoo.operators.sampling.rnd import FloatRandomSampling
    from pymoo.operators.integer_from_float_operator import IntegerFromFloatSampling
    from pymoo.operators.sampling.rnd import BinaryRandomSampling
    from pymoo.operators.sampling.rnd import PermutationRandomSampling

    SAMPLING = [
        ("real_random", FloatRandomSampling),
        ("real_lhs", LatinHypercubeSampling),
        ("bin_random", BinaryRandomSampling),
        ("int_random", IntegerFromFloatSampling, {'clazz': FloatRandomSampling}),
        ("int_lhs", IntegerFromFloatSampling, {'clazz': LatinHypercubeSampling}),
        ("perm_random", PermutationRandomSampling)
    ]

    return SAMPLING


def get_sampling(name, *args, d={}, **kwargs):
    return get_from_list(get_sampling_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Selection
# =========================================================================================================

def get_selection_options():
    from pymoo.operators.selection.rnd import RandomSelection
    from pymoo.operators.selection.tournament import TournamentSelection

    SELECTION = [
        ("random", RandomSelection),
        ("tournament", TournamentSelection)
    ]

    return SELECTION


def get_selection(name, *args, d={}, **kwargs):
    return get_from_list(get_selection_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Crossover
# =========================================================================================================

def get_crossover_options():
    from pymoo.operators.crossover.expx import ExponentialCrossover
    from pymoo.operators.crossover.hux import HalfUniformCrossover
    from pymoo.operators.crossover.pntx import PointCrossover
    from pymoo.operators.crossover.sbx import SimulatedBinaryCrossover
    from pymoo.operators.crossover.ux import UniformCrossover
    from pymoo.operators.crossover.pcx import PCX
    from pymoo.operators.integer_from_float_operator import IntegerFromFloatCrossover
    from pymoo.operators.crossover.erx import EdgeRecombinationCrossover
    from pymoo.operators.crossover.ox import OrderCrossover

    CROSSOVER = [
        ("real_sbx", SimulatedBinaryCrossover, dict(prob=0.9, eta=30)),
        ("int_sbx", IntegerFromFloatCrossover, dict(clazz=SimulatedBinaryCrossover, prob=0.9, eta=30)),
        ("real_pcx", PCX),
        ("(real|bin|int)_ux", UniformCrossover),
        ("(bin|int)_hux", HalfUniformCrossover),
        ("(real|bin|int)_exp", ExponentialCrossover),
        ("(real|bin|int)_one_point", PointCrossover, {'n_points': 1}),
        ("(real|bin|int)_two_point", PointCrossover, {'n_points': 2}),
        ("(real|bin|int)_k_point", PointCrossover),
        ("perm_ox", OrderCrossover),
        ("perm_erx", EdgeRecombinationCrossover)
    ]

    return CROSSOVER


def get_crossover(name, *args, d={}, **kwargs):
    return get_from_list(get_crossover_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Mutation
# =========================================================================================================

def get_mutation_options():
    from pymoo.operators.mutation.nom import NoMutation
    from pymoo.operators.mutation.bitflip import BitflipMutation
    from pymoo.operators.mutation.pm import PolynomialMutation
    from pymoo.operators.integer_from_float_operator import IntegerFromFloatMutation
    from pymoo.operators.mutation.inversion import InversionMutation

    MUTATION = [
        ("none", NoMutation, {}),
        ("real_pm", PolynomialMutation, dict(eta=20)),
        ("int_pm", IntegerFromFloatMutation, dict(clazz=PolynomialMutation, eta=20)),
        ("bin_bitflip", BitflipMutation),
        ("perm_inv", InversionMutation)
    ]

    return MUTATION


def get_mutation(name, *args, d={}, **kwargs):
    return get_from_list(get_mutation_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Termination
# =========================================================================================================

def get_termination_options():
    from pymoo.termination.max_eval import MaximumFunctionCallTermination
    from pymoo.termination.max_gen import MaximumGenerationTermination
    from pymoo.termination.max_time import TimeBasedTermination
    from pymoo.termination.xtol import DesignSpaceTermination
    from pymoo.termination.ftol import MultiObjectiveSpaceTermination
    from pymoo.termination.ftol import SingleObjectiveSpaceTermination
    from pymoo.termination.default import DefaultMultiObjectiveTermination, DefaultSingleObjectiveTermination

    TERMINATION = [
        ("n_eval", MaximumFunctionCallTermination),
        ("(n_gen|n_iter)", MaximumGenerationTermination),
        ("time", TimeBasedTermination),
        ("(x_tol|xtol)", DesignSpaceTermination),
        ("(f_tol$|ftol$)", MultiObjectiveSpaceTermination),
        ("(f_tol_s|ftol_s)", SingleObjectiveSpaceTermination),
        ("(default$|default_multi)", DefaultMultiObjectiveTermination),
        ("default_single$", DefaultSingleObjectiveTermination)
    ]

    return TERMINATION


def get_termination(name, *args, d={}, **kwargs):
    return get_from_list(get_termination_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Problems
# =========================================================================================================

def get_problem_options():
    from pymoo.problems.multi import BNH, Carside
    from pymoo.problems.multi import CTP1, CTP2, CTP3, CTP4, CTP5, CTP6, CTP7, CTP8
    from pymoo.problems.multi import DASCMOP1, DASCMOP2, DASCMOP3, DASCMOP4, DASCMOP5, DASCMOP6, DASCMOP7, DASCMOP8, \
        DASCMOP9
    from pymoo.problems.multi import MODAct, MW1, MW2, MW3, MW4, MW5, MW6, MW7, MW8, MW9, MW10, MW11, MW12, MW13, MW14
    from pymoo.problems.single import Ackley
    from pymoo.problems.many import DTLZ1, C1DTLZ1, DC1DTLZ1, DC1DTLZ3, DC2DTLZ1, DC2DTLZ3, DC3DTLZ1, DC3DTLZ3, C1DTLZ3, \
        C2DTLZ2, C3DTLZ1, C3DTLZ4, ScaledDTLZ1, ConvexDTLZ2, ConvexDTLZ4, DTLZ2, DTLZ3, DTLZ4, DTLZ5, DTLZ6, DTLZ7, \
        InvertedDTLZ1, WFG1, WFG2, WFG3, WFG4, WFG5, WFG6, WFG7, WFG8, WFG9
    from pymoo.problems.multi import Kursawe, OSY, SRN, TNK, Truss2D, WeldedBeam, ZDT1, ZDT2, ZDT3, ZDT4, ZDT5, ZDT6
    from pymoo.problems.single import CantileveredBeam, Griewank, Himmelblau, Knapsack, PressureVessel, Rastrigin, \
        Rosenbrock, Schwefel, Sphere, Zakharov
    from pymoo.problems.single import G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16, G17, G18, \
        G19, G20, G21, G22, G23, G24
    from pymoo.problems.dynamic.df import DF1, DF2, DF3, DF4, DF5, DF6, DF7, DF8, DF9, DF10, DF11, DF12, DF13, DF14

    PROBLEM = [
        ('ackley', Ackley),
        ('bnh', BNH),
        ('carside', Carside),
        ('ctp1', CTP1),
        ('ctp2', CTP2),
        ('ctp3', CTP3),
        ('ctp4', CTP4),
        ('ctp5', CTP5),
        ('ctp6', CTP6),
        ('ctp7', CTP7),
        ('ctp8', CTP8),
        ('dascmop1', DASCMOP1),
        ('dascmop2', DASCMOP2),
        ('dascmop3', DASCMOP3),
        ('dascmop4', DASCMOP4),
        ('dascmop5', DASCMOP5),
        ('dascmop6', DASCMOP6),
        ('dascmop7', DASCMOP7),
        ('dascmop8', DASCMOP8),
        ('dascmop9', DASCMOP9),
        ('df1', DF1),
        ('df2', DF2),
        ('df3', DF3),
        ('df4', DF4),
        ('df5', DF5),
        ('df6', DF6),
        ('df7', DF7),
        ('df8', DF8),
        ('df9', DF9),
        ('df10', DF10),
        ('df11', DF11),
        ('df12', DF12),
        ('df13', DF13),
        ('df14', DF14),
        ('modact', MODAct),
        ('mw1', MW1),
        ('mw2', MW2),
        ('mw3', MW3),
        ('mw4', MW4),
        ('mw5', MW5),
        ('mw6', MW6),
        ('mw7', MW7),
        ('mw8', MW8),
        ('mw9', MW9),
        ('mw10', MW10),
        ('mw11', MW11),
        ('mw12', MW12),
        ('mw13', MW13),
        ('mw14', MW14),
        ('dtlz1^-1', InvertedDTLZ1),
        ('dtlz1', DTLZ1),
        ('dtlz2', DTLZ2),
        ('dtlz3', DTLZ3),
        ('dtlz4', DTLZ4),
        ('dtlz5', DTLZ5),
        ('dtlz6', DTLZ6),
        ('dtlz7', DTLZ7),
        ('convex_dtlz2', ConvexDTLZ2),
        ('convex_dtlz4', ConvexDTLZ4),
        ('sdtlz1', ScaledDTLZ1),
        ('c1dtlz1', C1DTLZ1),
        ('c1dtlz3', C1DTLZ3),
        ('c2dtlz2', C2DTLZ2),
        ('c3dtlz1', C3DTLZ1),
        ('c3dtlz4', C3DTLZ4),
        ('dc1dtlz1', DC1DTLZ1),
        ('dc1dtlz3', DC1DTLZ3),
        ('dc2dtlz1', DC2DTLZ1),
        ('dc2dtlz3', DC2DTLZ3),
        ('dc3dtlz1', DC3DTLZ1),
        ('dc3dtlz3', DC3DTLZ3),
        ('cantilevered_beam', CantileveredBeam),
        ('griewank', Griewank),
        ('himmelblau', Himmelblau),
        ('knp', Knapsack),
        ('kursawe', Kursawe),
        ('osy', OSY),
        ('pressure_vessel', PressureVessel),
        ('rastrigin', Rastrigin),
        ('rosenbrock', Rosenbrock),
        ('schwefel', Schwefel),
        ('sphere', Sphere),
        ('srn', SRN),
        ('tnk', TNK),
        ('truss2d', Truss2D),
        ('welded_beam', WeldedBeam),
        ('zakharov', Zakharov),
        ('zdt1', ZDT1),
        ('zdt2', ZDT2),
        ('zdt3', ZDT3),
        ('zdt4', ZDT4),
        ('zdt5', ZDT5),
        ('zdt6', ZDT6),
        ('g1', G1),
        ('g2', G2),
        ('g3', G3),
        ('g4', G4),
        ('g5', G5),
        ('g6', G6),
        ('g7', G7),
        ('g8', G8),
        ('g9', G9),
        ('g10', G10),
        ('g11', G11),
        ('g12', G12),
        ('g13', G13),
        ('g14', G14),
        ('g15', G15),
        ('g16', G16),
        ('g17', G17),
        ('g18', G18),
        ('g19', G19),
        ('g20', G20),
        ('g21', G21),
        ('g22', G22),
        ('g23', G23),
        ('g24', G24),
        ('wfg1', WFG1),
        ('wfg2', WFG2),
        ('wfg3', WFG3),
        ('wfg4', WFG4),
        ('wfg5', WFG5),
        ('wfg6', WFG6),
        ('wfg7', WFG7),
        ('wfg8', WFG8),
        ('wfg9', WFG9)
    ]

    return PROBLEM


def get_problem(name, *args, d={}, **kwargs):
    if name.startswith("go-"):
        from pymoo.vendor.global_opt import get_global_optimization_problem_options
        return get_from_list(get_global_optimization_problem_options(), name.lower(), args, {**d, **kwargs})
    elif name.startswith("bbob-"):
        from pymoo.vendor.vendor_coco import COCOProblem
        return COCOProblem(name.lower(), **kwargs)
    else:
        return get_from_list(get_problem_options(), name.lower(), args, {**d, **kwargs})


# =========================================================================================================
# Weights
# =========================================================================================================

def get_reference_direction_options():
    from pymoo.util.reference_direction import UniformReferenceDirectionFactory
    from pymoo.util.reference_direction import MultiLayerReferenceDirectionFactory
    from pymoo.util.ref_dirs.reduction import ReductionBasedReferenceDirectionFactory
    from pymoo.util.ref_dirs.energy import RieszEnergyReferenceDirectionFactory
    from pymoo.util.ref_dirs.energy_layer import LayerwiseRieszEnergyReferenceDirectionFactory

    REFERENCE_DIRECTIONS = [
        ("(das-dennis|uniform)", UniformReferenceDirectionFactory),
        ("multi-layer", MultiLayerReferenceDirectionFactory),
        ("(energy|riesz)", RieszEnergyReferenceDirectionFactory),
        ("(layer-energy|layer-riesz)", LayerwiseRieszEnergyReferenceDirectionFactory),
        ("red", ReductionBasedReferenceDirectionFactory)
    ]

    return REFERENCE_DIRECTIONS


def get_reference_directions(name, *args, d={}, **kwargs):
    return get_from_list(get_reference_direction_options(), name, args, {**d, **kwargs}).do()


# =========================================================================================================
# Visualization
# =========================================================================================================

def get_visualization_options():
    from pymoo.visualization.pcp import PCP
    from pymoo.visualization.petal import Petal
    from pymoo.visualization.radar import Radar
    from pymoo.visualization.radviz import Radviz
    from pymoo.visualization.scatter import Scatter
    from pymoo.visualization.star_coordinate import StarCoordinate
    from pymoo.visualization.heatmap import Heatmap
    from pymoo.visualization.fitness_landscape import FitnessLandscape

    VISUALIZATION = [
        ("scatter", Scatter),
        ("heatmap", Heatmap),
        ("pcp", PCP),
        ("petal", Petal),
        ("radar", Radar),
        ("radviz", Radviz),
        ("star", StarCoordinate),
        ("fitness-landscape", FitnessLandscape)
    ]

    return VISUALIZATION


def get_visualization(name, *args, d={}, **kwargs):
    return get_from_list(get_visualization_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Performance Indicator
# =========================================================================================================


def get_performance_indicator_options():
    from pymoo.indicators.gd import GD
    from pymoo.indicators.gd_plus import GDPlus
    from pymoo.indicators.igd import IGD
    from pymoo.indicators.igd_plus import IGDPlus
    from pymoo.indicators.hv import Hypervolume
    from pymoo.indicators.rmetric import RMetric

    PERFORMANCE_INDICATOR = [
        ("gd", GD),
        ("gd+", GDPlus),
        ("igd", IGD),
        ("igd+", IGDPlus),
        ("hv", Hypervolume),
        ("rmetric", RMetric)
    ]
    return PERFORMANCE_INDICATOR


def get_performance_indicator(name, *args, d={}, **kwargs):
    return get_from_list(get_performance_indicator_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# DECOMPOSITION
# =========================================================================================================

def get_decomposition_options():
    from pymoo.decomposition.pbi import PBI
    from pymoo.decomposition.tchebicheff import Tchebicheff
    from pymoo.decomposition.weighted_sum import WeightedSum
    from pymoo.decomposition.asf import ASF
    from pymoo.decomposition.aasf import AASF
    from pymoo.decomposition.perp_dist import PerpendicularDistance

    DECOMPOSITION = [
        ("weighted-sum", WeightedSum),
        ("tchebi", Tchebicheff),
        ("pbi", PBI),
        ("asf", ASF),
        ("aasf", AASF),
        ("perp_dist", PerpendicularDistance)
    ]

    return DECOMPOSITION


def get_decomposition(name, *args, d={}, **kwargs):
    return get_from_list(get_decomposition_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# DECOMPOSITION
# =========================================================================================================

def get_decision_making_options():
    from pymoo.mcdm.high_tradeoff import HighTradeoffPoints
    from pymoo.mcdm.pseudo_weights import PseudoWeights

    DECISION_MAKING = [
        ("high-tradeoff", HighTradeoffPoints),
        ("pseudo-weights", PseudoWeights)
    ]

    return DECISION_MAKING


def get_decision_making(name, *args, d={}, **kwargs):
    return get_from_list(get_decision_making_options(), name, args, {**d, **kwargs})


# =========================================================================================================
# Documentation
# =========================================================================================================


def dummy(name, kwargs):
    """
    A convenience method to get a {type} object just by providing a string.

    Parameters
    ----------

    name : {{ {options} }}
        Name of the {type}.

    kwargs : dict
        Dictionary that should be used to call the method mapped to the {type} factory function.

    Returns
    -------
    class : {clazz}
        An {type} object based on the string. `None` if the {type} was not found.

    """
    pass


def options_to_string(l):
    return ", ".join(["'%s'" % k[0] for k in l])


if Config.parse_custom_docs:
    from pymoo.docs import parse_doc_string

    from pymoo.factory import get_algorithm_options, get_selection_options, get_crossover_options, \
        get_mutation_options, get_termination_options, get_algorithm, get_selection, get_crossover, get_mutation, \
        get_termination, get_sampling, get_sampling_options

    parse_doc_string(dummy, get_algorithm, {"type": "algorithm",
                                            "clazz": ":class:`~pymoo.core.algorithm.Algorithm`",
                                            "options": options_to_string(get_algorithm_options())
                                            })

    parse_doc_string(dummy, get_sampling, {"type": "sampling",
                                           "clazz": ":class:`~pymoo.core.sampling.Sampling`",
                                           "options": options_to_string(get_sampling_options())
                                           })

    parse_doc_string(dummy, get_selection, {"type": "selection",
                                            "clazz": ":class:`~pymoo.core.selection.Selection`",
                                            "options": options_to_string(get_selection_options())
                                            })

    parse_doc_string(dummy, get_crossover, {"type": "crossover",
                                            "clazz": ":class:`~pymoo.core.crossover.Crossover`",
                                            "options": options_to_string(get_crossover_options())
                                            })

    parse_doc_string(dummy, get_mutation, {"type": "mutation",
                                           "clazz": ":class:`~pymoo.core.mutation.Mutation`",
                                           "options": options_to_string(get_mutation_options())
                                           })

    parse_doc_string(dummy, get_termination, {"type": "termination",
                                              "clazz": ":class:`~pymoo.core.termination.termination`",
                                              "options": options_to_string(get_termination_options())
                                              })
