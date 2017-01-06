#!/usr/bin/env python

# ---- MODULE DOCSTRING

__doc__ = """

(C) Forest Evolution Algorithm, Romain Wuilbercq, 2017

    ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
   /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\
   /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\
   /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\

Description:
-----------

This example shows how to use the Forest Evolution to solve a simple
non-constrained optimisation problem with both a local and a global optimum.

"""

# ---- IMPORT MODULES

import math

from Forest import Utilities
from Forest import Forest as opt

# ---- CREATE TEST CASE

def evaluator(vector):
    """

    The function has two optimum solutions, the global
    at around (0.63,0.16) and a local at (0.5, 0.5).

    """

    r1 = (vector[0] - 0.5)**2 + (vector[1] - 0.5)**2
    r2 = (vector[0] - 0.6)**2 + (vector[1] - 0.1)**2
    s1, s2 = 0.3, 0.03
    return 2 - (0.80 * math.exp(-r1**2 / s1**2) + 0.88 * math.exp(-r2**2 / s2**2))


# ---- SOLVE TEST CASE WITH FOREST EVOLUTION ALGORITHM

def run():

    # creates model
    ndim = 2
    model = opt.Forest(lower=[0] * ndim,
                        upper=[1] * ndim,
                        fun=evaluator,
                        max_std=0.2,
                        min_std=0.2,
                        init_numb_trees=20,
                        max_numb_trees=50,
                        max_seeds=10,
                        min_seeds=2,
                        epsilon=0.1,
                        epsilon_decay=0.0,
                        max_iters=100,
                        mut_proba=0.1,
                        )

    # runs model
    cost = model.run()

    # plots convergence
    Utilities.ConvergencePlot(cost)

    # prints out best solution
    solution = model.population[0][1].vector
    print("Fitness Value FEA: {0} | Solution: {1}".format(model.population[0][0], solution))


if __name__ == "__main__":
    run()


# ---- END
