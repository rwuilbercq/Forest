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

This example shows how to use the Forest Evolution to solve the 10-dimensional
Rastrigin's function.

"""

# ---- IMPORT MODULES

try:
    import numpy as np
except:
    raise ImportError("Numpy module not installed.")

from Forest import Forest as opt
from Forest import Utilities

# ---- CREATE TEST CASE

def evaluator(vector):
    """
    A n-dimensional Rastrigin's function is defined as:

                            n
            f(x) = 10*n + Sigma { x_i^2 - 10*cos(2*PI*x_i) }
                           i=1

    where  -5.12 <= x_i <= 5.12.

    Thus the global minima of the function being f(x) = 0 at all x_i = 0.

    """

    vector = np.array(vector)

    return 10 * vector.size + sum(vector*vector - 10 * np.cos(2 * np.pi * vector))


# ---- SOLVE TEST CASE WITH FOREST EVOLUTION ALGORITHM

def run():

    # creates model
    ndim = int(10)
    model = opt.Forest(lower = [-5.12]*ndim   ,
                       upper = [ 5.12]*ndim   ,
                       fun   = evaluator      ,
                       max_std = 1            ,
                       min_std = 0.3          ,
                       init_numb_trees =   5  ,
                       max_numb_trees  =  50  ,
                       max_seeds       =  50  ,
                       min_seeds       =   5  ,
                       epsilon         =   0.1,
                       epsilon_decay   =   0.0,
                       max_iters       =  60  ,
                       mut_proba       =   0.1,)

    # runs model
    cost = model.run()

    # plots convergence
    Utilities.ConvergencePlot(cost)

    # prints out best solution
    solution = model.population[0][1]
    print("Fitness Value FEA: {0}".format(model.population[0][0]))


if __name__ == "__main__":
    run()


# ---- END
