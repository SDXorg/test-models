"""
Python model test-models/tests/lookups/test_lookups.py
Translated using PySD version 0.7.5
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'TIME STEP': 'time_step',
    'FINAL TIME': 'final_time',
    'SAVEPER': 'saveper',
    'lookup function table': 'lookup_function_table',
    'accumulation': 'accumulation',
    'lookup function call': 'lookup_function_call',
    'INITIAL TIME': 'initial_time',
    'TIME': 'time',
    'rate': 'rate',
    'Time': 'time'
}


@cache('step')
def lookup_function_call():
    """
    lookup function call
    --------------------
    (lookup_function_call)


    """
    return lookup_function_table(time())


integ_accumulation = functions.Integ(lambda: rate(), lambda: 0)


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


def lookup_function_table(x):
    """
    lookup function table
    ---------------------
    (lookup_function_table)


    """
    return functions.lookup(x, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
                            [0, 0, 1, 1, 0, 0, -1, -1, 0, 0])


@cache('step')
def accumulation():
    """
    accumulation
    ------------
    (accumulation)


    """
    return integ_accumulation()


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


@cache('step')
def rate():
    """
    rate
    ----
    (rate)


    """
    return lookup_function_call()


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
