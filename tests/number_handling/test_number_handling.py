"""
Python model test-models/tests/number_handling/test_number_handling.py
<<<<<<< HEAD
Translated using PySD version 0.7.9
=======
Translated using PySD version 0.7.7
>>>>>>> origin/master
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'equality': 'equality',
    'denominator': 'denominator',
    'numerator': 'numerator',
    'quotient': 'quotient',
    'quotient target': 'quotient_target',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'}


@cache('step')
def equality():
    """
    equality




    """
    return functions.if_then_else(quotient() == quotient_target(), 1, 0)


@cache('run')
def denominator():
    """
    denominator




    """
    return 4


@cache('run')
def numerator():
    """
    numerator




    """
    return 3


@cache('step')
def quotient():
    """
    quotient




    """
    return numerator() / denominator()


@cache('run')
def quotient_target():
    """
    quotient target




    """
    return 0.75


@cache('run')
def final_time():
    """
    FINAL TIME

    Month

    The final time for the simulation.
    """
    return 1


@cache('run')
def initial_time():
    """
    INITIAL TIME

    Month

    The initial time for the simulation.
    """
    return 0


@cache('step')
def saveper():
    """
    SAVEPER

    Month [0,?]

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    TIME STEP

    Month [0,?]

    The time step for the simulation.
    """
    return 1
