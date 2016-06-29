
"""
Python model test-models/tests/lookups/test_lookups.py
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
    'lookup function table': 'lookup_function_table',
    'TIME STEP': 'time_step',
    'FINAL TIME': 'final_time',
    'rate': 'rate',
    'SAVEPER': 'saveper',
    'lookup function call': 'lookup_function_call',
    'accumulation': 'accumulation'}


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Minute
    The final time for the simulation.
    """
    return 45


@cache('step')
def _daccumulation_dt():
    """
    Implicit
    --------
    (_daccumulation_dt)
    See docs for accumulation
    Provides derivative for accumulation function
    """
    return rate()


def _init_accumulation():
    """
    Implicit
    --------
    (_init_accumulation)
    See docs for accumulation
    Provides initial conditions for accumulation function
    """
    return 0


@cache('step')
def lookup_function_call():
    """
    lookup function call
    --------------------
    (lookup_function_call)


    """
    return lookup_function_table(time())


@cache('step')
def rate():
    """
    rate
    ----
    (rate)


    """
    return lookup_function_call()


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Minute [0,?]
    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Minute
    The initial time for the simulation.
    """
    return 0


def lookup_function_table(x):
    """
    lookup function table
    ---------------------
    (lookup_function_table)


    """
    return functions.lookup(
        x, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
        [0, 0, 1, 1, 0, 0, -1, -1, 0, 0])


@cache('step')
def time():
    """
    Time
    ----
    (time)
    None
    The time of the model
    """
    return _t


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Minute [0,?]
    The time step for the simulation.
    """
    return 0.25


@cache('step')
def accumulation():
    """
    accumulation
    ------------
    (accumulation)


    """
    return _state['accumulation']


def time():
    return _t
functions.time = time
functions.initial_time = initial_time
