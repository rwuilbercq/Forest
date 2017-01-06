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

# ---- IMPORT MODULE(S)
from distutils.core import setup

# ---- SETUP INFORMATION
setup(name         = "Forest",
      version      = "x.x.x",
      description  = "Forest optimisation Algorithm",
      author       = "Romain Wuilbercq",
      author_email = "romain.wuilbercq@gmail.com",
      url          = "https://github.com/rwuilbercq/Forest",
      keywords     = ["optimisation", "swarm", "stochastic", "global"],
      classifiers  = [
          "Programming Language :: Python",
          "Development Status :: Beta",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3"
      ],
      long_description = """

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

      """)
