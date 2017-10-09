"""
Python model test-models/tests/lookups/test_lookups.py
Translated using PySD version 0.7.12
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'Lookup Linebreak Before Comma': 'lookup_linebreak_before_comma',
    'lookup function call': 'lookup_function_call',
    'rate': 'rate',
    'accumulation': 'accumulation',
    'lookup function table': 'lookup_function_table',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'}


def lookup_linebreak_before_comma(x):
    """
    Lookup Linebreak Before Comma



    lookup

    This lookup has a line break before the comma.
    """
    return functions.lookup(x, [0, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4], [
        1, 1, 0.98, 0.9, 0.75, 0.45, 0.25, 0.17, 0.14, 0.12, 0.11, 0.1, 0.1])


@cache('step')
def lookup_function_call():
    """
    lookup function call



    component


    """
    return lookup_function_table(time())


@cache('step')
def rate():
    """
    rate



    component


    """
    return lookup_function_call()


@cache('step')
def accumulation():
    """
    accumulation



    component


    """
    return integ_accumulation()


def lookup_function_table(x):
    """
    lookup function table



    lookup


    """
    return functions.lookup(x, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45], [
        0, 0, 1, 1, 0, 0, -1, -1, 0, 0])


@cache('run')
def final_time():
    """
    FINAL TIME

    Minute

    constant

    The final time for the simulation.
    """
    return 45


@cache('run')
def initial_time():
    """
    INITIAL TIME

    Minute

    constant

    The initial time for the simulation.
    """
    return 0


@cache('step')
def saveper():
    """
    SAVEPER

    Minute [0,?]

    component

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    TIME STEP

    Minute [0,?]

    constant

    The time step for the simulation.
    """
    return 0.25


integ_accumulation = functions.Integ(lambda: rate(), lambda: 0)
