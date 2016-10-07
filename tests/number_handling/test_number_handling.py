
"""
Python model test-models/tests/number_handling/test_number_handling.py
Translated using PySD version 0.7.2
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'Time': 'time',
    'INITIAL TIME': 'initial_time',
    'TIME': 'time',
    'SAVEPER': 'saveper',
    'denominator': 'denominator',
    'numerator': 'numerator',
    'TIME STEP': 'time_step',
    'FINAL TIME': 'final_time',
    'quotient target': 'quotient_target',
    'quotient': 'quotient',
    'equality': 'equality'}


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Month [0,?]
    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Month
    The final time for the simulation.
    """
    return 1


@cache('step')
def equality():
    """
    equality
    --------
    (equality)


    """
    return functions.if_then_else(quotient() == quotient_target(), 1, 0)


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Month
    The initial time for the simulation.
    """
    return 0


@cache('run')
def denominator():
    """
    denominator
    -----------
    (denominator)


    """
    return 4


@cache('run')
def numerator():
    """
    numerator
    ---------
    (numerator)


    """
    return 3


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Month [0,?]
    The time step for the simulation.
    """
    return 1


@cache('step')
def quotient():
    """
    quotient
    --------
    (quotient)


    """
    return numerator() / denominator()


@cache('run')
def quotient_target():
    """
    quotient target
    ---------------
    (quotient_target)


    """
    return 0.75
