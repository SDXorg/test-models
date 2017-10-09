"""
Python model test-models/tests/number_handling/test_number_handling.py
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
    'time': 'time',
    'TIME STEP': 'time_step',
    'INITIAL TIME': 'initial_time',
    'FINAL TIME': 'final_time',
    'equality': 'equality',
    'quotient target': 'quotient_target',
    'quotient': 'quotient',
    'numerator': 'numerator',
    'SAVEPER': 'saveper',
    'denominator': 'denominator'}


@cache('step')
def equality():
    """
    equality



    component


    """
    return (functions.if_then_else(quotient() == quotient_target(), 1, 0))


@cache('run')
def quotient_target():
    """
    quotient target



    constant


    """
    return 0.75


@cache('step')
def quotient():
    """
    quotient



    component


    """
    return numerator() / denominator()


@cache('run')
def numerator():
    """
    numerator



    constant


    """
    return 3


@cache('run')
def denominator():
    """
    denominator



    constant


    """
    return 4


@cache('run')
def initial_time():
    """
    INITIAL TIME

    Months

    constant

    The initial time for the simulation.
    """
    return 0


@cache('run')
def final_time():
    """
    FINAL TIME

    Months

    constant

    The final time for the simulation.
    """
    return 1


@cache('run')
def time_step():
    """
    TIME STEP

    Months

    constant

    The time step for the simulation.
    """
    return 1


@cache('run')
def saveper():
    """
    SAVEPER

    Months

    constant

    The time step for the simulation.
    """
    return time_step()
