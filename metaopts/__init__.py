from . import utilities
from . import algorithms
from .utilities.fitness import create_fitness_function
from .algorithms.avoa import avoa
from .algorithms.dgo import dgo
from .algorithms.ga import ga
from .algorithms.mvo import mvo
from .algorithms.stbo import stbo


__all__ = [
    'create_fitness_function',
    'avoa',
    'dgo',
    'ga',
    'mvo',
    'stbo',
]
__version__ = '0.0.1'
__author__ = 'https://github.com/DrKarambit'
