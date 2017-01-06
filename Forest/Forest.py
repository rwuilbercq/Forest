#!/usr/bin/env python

# ---- MODULE DOCSTRING

__doc__ = """

(C) Forest Evolution Algorithm, Romain Wuilbercq, 2017

    ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
   /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\
   /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\
   /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\

The **Forest Evolution Algorithm (FEA)** is based on the
seed dispersal mechanism employed by trees to colonize
forest areas.

Its implementation is a variant of the Invasive Weed
Algorithm (IWA).

"""

# ---- IMPORT MODULES

import random
import copy
import queue

import numpy as np

# ---- TREE CLASS

class Tree(object):
    """ Creates an individual tree. """

    def __init__(self, lower, upper):
        """ Initialises a tree object. """

        self.vector  = self._initialise(lower, upper)
        self.seeds   = 0
        self.year    = 0
        self.valid   = True

    def _initialise(self, lower, upper):
        """ Initialises solution vector. """

        vector = []
        for i in range(len(lower)):
            vector.append( lower[i] + random.random() * (upper[i] - lower[i]) )
        return vector

    def __cmp__(self, other):
        """ Tree object comparison method. """

        if hasattr(other, 'year'):
            return self.year.__cmp__(other.year)

    def __eq__(self, other):
        """ Tree object equality test. """

        if hasattr(other, 'vector'):
            return self.vector == other.vector

    def __ne__(self, other):
        """ Tree object non equality test. """

        if hasattr(other, 'vector'):
            return self.vector != other.vector

# ---- FOREST CLASS

class Forest(object):
    """

    Creates a Forest Evolution Algorithm (FEA) model.

    The Forest Evolution Algorithm (FEA) algorithm is adapted
    from the Invasive Weed Optimisation (IWO) evolutionary
    algorithm and mimicks the seed dispersal mechanism used
    by trees to colonize areas of forest land.

    """

    def run(self, verbose=False):
        """ Runs a forest optimisation algorithm. """

        cost = {}; cost["best"] = []; cost["mean"] = []
        for i in range(self.max_iters):

            # prints out information at current cycle
            if verbose:
                print("Iteration: {}".format(i),
                      "Fitness: {}".format(self.forest[0][0]))

            # reproduction phase
            self.reproduce()

            # seed dispersal phase
            self.seedlings = []
            for tree in self.population:
                self.disperse(tree[1])
                tree[1].year += 1

            # selection phase
            self.select()

            # decays exploration parameters
            if (self.epsilon > 0):
                self.epsilon -= self.epsilon_decay

            # stores statistics and updates counter of iterations
            cost["best"].append(self.population[0][0])
            cost["mean"].append( sum( [ tree[0] for tree in self.population ] )\
                                 / len(self.population) )
            self.iteration += 1

        return cost

    def __init__(self,
                 lower, upper            ,
                 fun                     ,
                 max_std, min_std        ,
                 init_numb_trees =  10   ,
                 max_numb_trees  =  20   ,
                 max_seeds       =  10   ,
                 min_seeds       =   1   ,
                 epsilon         =   0.1 ,
                 epsilon_decay   =   0.0 ,
                 max_iters       = 100   ,
                 mut_proba       =   0.1 ,
                 seed            = None  ,
                ):
        """

        1. INITIALISATION PHASE.
        -----------------------

        Generates an initial population of tree(s).

        The initial population should cover the entire search space as
        much as possible by uniformly randomizing individuals within
        the search space constrained by the prescribed lower and
        upper bounds.

        Parameters:
        ----------

            :param list lower          : lower bound of solution vector
            :param list upper          : upper bound of solution vector
            :param def fun             : evaluation function (e.g. fitness or novelty)
            :param int init_numb_trees : initial size of the forest
            :param int max_numb_trees  : maximum size of the forest
            :param int max_seeds       : maximum number of seeds during reproduction
            :param int min_seeds       : maximum number of seeds during reproduction
            :param float epsilon       : exploration parameter
            :param float epsilon_decay : decay rate of exploration parameter per year
            :param int max_iters       : maximum number of generations
            :param int max_std         : maximum standard deviation for search around existing solution
            :param int min_std         : minimum standard deviation for search around existing solution
            :param float mut_proba     : probability of mutation
            :param int seed            : seed for random number generator

        """

        # generates a seed for the random number generator
        if (seed == None):
            self.seed = random.randint(0, 1000)
        else:
            self.seed = seed
        random.seed(self.seed)

        # assigns properties of FO algorithm
        self.max_number_trees = max_numb_trees
        self.max_seeds        = max_seeds
        self.min_seeds        = min_seeds
        self.epsilon          = epsilon
        self.epsilon_decay    = epsilon_decay
        self.max_iters        = max_iters
        self.max_std          = max_std
        self.min_std          = min_std
        self.mut_proba        = mut_proba

        # assigns fitness function
        self.evaluate = fun

        # stores lower and upper bounds
        self.lower = lower
        self.upper = upper

        # evaluates dimension of the optimal problem
        assert ( len(lower)==len(upper) ), \
               "'lower' and 'upper' must be of the same dimension."
        self.dim = len(lower)

        # initialises a forest of trees
        self.population = []
        for _ in range(init_numb_trees):
            tree = Tree(lower, upper)
            if (fun != None):
                self.population.append((fun(tree.vector), tree))
            else:
                self.population.append((sys.float_info.max, tree))

        # initialises iterations counter
        self.iteration = 1

        # creates a seedlings buffer
        self.seedlings = []

    def select(self):
        """

        2. SELECTION PHASE.
        ------------------

        If a tree does not reproduce, it becomes extinct. Thus, this
        leads to the requirement of a competitive exclusion in order to
        eliminate those trees with lower metric values.

        This is done to limit the maximum number of trees in the forest.
        Initially, fast reproduction of trees take place and all of them
        are included in the forest. The fitter trees reproduce more than
        the undesirable ones. Here, "fitter" is either in terms of objective
        or novelty (in novelty search).

        This elimination mechanism is activated when the population exceeds
        the pre-selected maximum number of trees in the forest.

        To do so, the trees and their seeds are ranked and those with lower
        fitness values are removed to sustain a manageable tree population.

        """

        def truncate(self):
            """ Truncates forest to maximum number of trees. """

            self.population = self.population[:self.max_number_trees]

        def SortOnItem(list_, item_loc):
            """ Sorts based on a given item. """

            templist = [elmt[item_loc] for elmt in list_]
            index = np.argsort(templist)
            return [list_[i] for i in index]

        # adds current seedlings to forest
        for tree in self.seedlings:

            # if tree does not competes with another existing one, adds it
            if tree not in self.population:
                self.population.append(tree)

        # sorts the trees of the forest in ascending values - minimization
        self.population = SortOnItem(self.population, item_loc=0)

        # removes unfit trees from forest
        truncate(self)

    def reproduce(self):
        """

        3. REPRODUCTION PHASE.
        ---------------------

        The trees will produce seeds based on their relative fitness which
        will then be spread over the problem space. Each seed, in turn, will
        grow into a new tree depending on external factors.

        A linear increase in the number of seeds produced by the trees of the
        forest is considered from max_seeds for the tree with the lowest value
        to min_seeds for the one with the highest value (i.e. minimization
        problem).

        """

        def compute_seeds(fitness):
            """ Computes the number of seeds given a fitness value. """

            seeds = (fitness-min_fitness) / (max_fitness-min_fitness) * \
                    (self.max_seeds-self.min_seeds) + self.min_seeds

            return round(seeds)

        # evaluates max and min fitness for current year
        max_fitness = max(tree[0] for tree in self.population)
        min_fitness = min(tree[0] for tree in self.population)

        # computes the number of seeds produced per tree
        for tree in self.population:
            tree[1].seeds = int(compute_seeds(tree[0]))

    def disperse(self, tree, dtype="normal", n=2):
        """

        4. SEED DISPERSAL PHASE.
        -----------------------

        Seed dispersal is the movement or transport of seeds away from
        the parent tree.

        Seeds are randomly distributed over the dimensional search space
        by random numbers drawn from either a normal distribution or a
        uniform distribution.

        In the biology of dispersal, a dispersal vector is "an agent
        transporting seeds or other dispersal units". Dispersal vectors
        may include biotic factors, such as animals, or abiotic factors,
        such as the wind or the ocean.

        Seeding can either be local (within a dispersal spread around the
        mother tree) or global, in which case, a dispersal vector
        transports a seed over a long distance away from the mother tree's
        location to colonize new areas of forest - i.e. exploration phase.

        Parameters:
        ----------

            :param Tree tree : an individual tree object
            :param str dtype : distribution type for seeding around mother tree
            :param int n     : index factor for dispersal spread evaluation

        """

        # computes "dispersion spread" for current generation
        spread = self._dispersion_spread(n)

        # creates mother tree's offsprings known as seedlings
        for _ in range(tree.seeds):

            # creates new seedling by mutation of mother tree's DNA
            seedling = self._mutate(tree, spread, dtype)

            # checks boundaries of optimal problem
            self._check(seedling.vector)

            # evaluates fitness
            fitness = self.evaluate(seedling.vector)

            # adds new seedling to forest
            self.seedlings.append((fitness, seedling))

    def _mutate(self, tree, spread, dtype):
        """

        Creates a seedling by randomly mutating the DNA of its mother tree.

        For each seed, a coin toss decides whether a local or global
        seeding takes place to ensure constant exploration of the
        search space.

        Parameters:
        ----------

            :param Tree tree    : an individual tree object
            :param float spread : dispersion spread, i.e. standard deviation
            :param str dtype    : distribution type

        """

        # defines wrapper functions
        def uniform(lower, upper):
            """
            Draws a random float number from a uniform distribution
            given by U[lower, upper].
            """

            return lower + random.random() * (upper - lower)

        def normal(mean, std):
            """
            Draws a random float number from a normal distribution
            with mean 'mu' and standard deviation 'sigma': N[mu, sigma].
            """

            return random.gauss(mean, std)

        # creates a seedling based on the DNA of its mother tree
        new_tree = copy.deepcopy(tree)

        # trade-off between exploitation and exploration
        if (random.random() > self.epsilon):

            # mutates initial solution vector - i.e. local seeding
            for i in range(self.dim):
                if (random.random() < self.mut_proba):
                    if (dtype == "normal"):
                        new_tree.vector[i] += normal(0, spread)

                    elif (dtype == "uniform"):
                        new_tree.vector[i] += uniform(-1, 1)

                    else:
                        raise AttributeError("'dtype' must either be 'normal' or 'uniform'.")

        else:

            # explores new region of the search space - i.e. global seeding
            new_tree = Tree(self.lower, self.upper)

        return new_tree

    def _dispersion_spread(self, n):
        """

        Computes standard deviation for current generation
        search.

        """

        return pow(self.max_iters-self.iteration, n) / pow(self.max_iters, n) * \
               (self.max_std - self.min_std) + self.min_std

    def _check(self, vector):
        """

        Checks that the solution vector is within optimal
        problem's boundaries.

        """

        for i, elmt in enumerate(vector):

            # checks lower bound
            if  (elmt < self.lower[i]):
                vector[i] = self.lower[i]

            # checks upper bound
            elif (elmt > self.upper[i]):
                vector[i] = self.upper[i]

        return vector

# ---- END
