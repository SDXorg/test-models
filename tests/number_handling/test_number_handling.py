
"""
Python model test-models/tests/number_handling/test_number_handling.py
Translated using PySD version 0.5.1
"""
from __future__ import division
import numpy as np
from pysd import utils

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'INITIAL TIME': 'initial_time',
    'equality': 'equality',
    'quotient target': 'quotient_target',
    'TIME STEP': 'time_step',
    'denominator': 'denominator',
    'numerator': 'numerator',
    'FINAL TIME': 'final_time',
    'SAVEPER': 'saveper',
    'quotient': 'quotient'}


@cache('step')
def equality():
    """
    equality
    --------
    (equality)


    """
    return functions.if_then_else(quotient() == quotient_target(), 1, 0)


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
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Month [0,?]
    The time step for the simulation.
    """
    return 1


@cache('run')
def quotient_target():
    """
    quotient target
    ---------------
    (quotient_target)


    """
    return 0.75


@cache('step')
def quotient():
    """
    quotient
    --------
    (quotient)


    """
    return numerator() / denominator()


def time():
    return _t
functions.time = time
functions.initial_time = initial_time
