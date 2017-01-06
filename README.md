<div style="text-align:center">
  <img src="../../assets/logo/Fea.png">
</div>

🌳**Forest** implements a simple **Forest Evolution Algorithm (FEA)**. The idea behind **Forest** is based on the seed dispersal mechanism employed by trees to colonize nearby and far away land areas. Seed dispersal is the movement or transport of seeds away from the parent tree. This implementation is a variant of the **Invasive Weed Algorithm** (see **ref. ➀**).

**Forest** is not implemented with **speed** in mind but instead, is a straightforward implementation of the underlying algorithm. 

# Intuition

--------------------------------------------------------------------------------

In the biology of dispersal, a **dispersal vector** is an agent transporting seeds (or whatever dispersal units). Dispersal vectors may include biotic factors, such as animals, or abiotic factors, such as the wind or the ocean. Seeding - i.e. seed dispersal - can either be local - i.e. within a dispersal spread around the mother tree (exploitation phase) - or global, in which case, a dispersal vector transports a seed over a long distance away from the location of the mother tree in order to colonize new lands - i.e. exploration phase.

In nature, if a tree does not reproduce, its species becomes extinct. Thus, this leads to the requirement of a competitive exclusion in order to eliminate (not always) those trees that do not reproduce - i.e. potentially "bad" solutions. This is done to limit the maximum number of trees in the forest. Initially, fast reproduction of trees take place and all of them are given a chance to be part of the growing forest. The fitter trees reproduce more than the undesirable ones, however. An elimination mechanism is then activated when the population exceeds a sustainable number of trees within the forest land - i.e. search space.

# Algorithm

--------------------------------------------------------------------------------

The FEA model of **Forest** consists of four phases that are accomplished sequentially, namely

➊ An **Initialisation Phase** where the initial population is generated to cover the entire search space as much as possible by uniformly randomizing individuals within the search space constrained by the prescribed lower and upper bounds.

➋ A **Selection Phase** (competitive exclusion) where trees with lower metric values might be eliminated from the forest. To do so, the trees are ranked and those with lower fitness values are removed to sustain a sustainable population of trees.

➌ A **Reproduction Phase** during which the trees will produce seeds based on their relative fitness. Seedlings - i.e. young plants - are created by randomly mutating the DNA of the mother trees. A linear increase in the number of seeds produced by the trees of the forest is considered from a maximum number of seeds for the tree with the lowest value to a minimum number of seeds for the tree with the highest fitness value - i.e. minimization problem.

➍ A **Dispersal Phase** where seeds are randomly distributed over the dimensional search space by random numbers drawn from either a normal distribution or a uniform distribution. For each seed, a coin toss decides whether a local or global seeding takes place to ensure constant exploration of the search space.

## Citation

--------------------------------------------------------------------------------

If you use this module in your projects (_whatever those are for!_), I would like to hear from you, I am curious! Of course, you do not have to, but you can drop me a line at: <romain.wuilbercq@gmail.com>

Suggestion:

> Wuilbercq, R., Forest Optimisation Python Library, 2017.

### Reference(s)

--------------------------------------------------------------------------------

➀ A. R. Mehrabian, C. Lucas, "A novel numerical optimization algorithm inspired from weed colonization," _Ecological Informatics_, vol. 1, pp. 355-366, 2006

### License

--------------------------------------------------------------------------------

#### The MIT License (MIT)

Copyright (C) 2017 Romain Wuilbercq

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
