
"""
Python model test-models/samples/SIR/SIR.py
Translated using PySD version 0.6.4
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'Total Population': 'total_population',
    'Recovering': 'recovering',
    'Susceptible': 'susceptible',
    'TIME STEP': 'time_step',
    'TIME': 'time',
    'SAVEPER': 'saveper',
    'Infectious': 'infectious',
    'Contact Infectivity': 'contact_infectivity',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'Time': 'time',
    'Duration': 'duration',
    'Succumbing': 'succumbing',
    'Recovered': 'recovered'}


@cache('run')
def total_population():
    """
    Total Population
    ----------------
    (total_population)
    Persons
    This is just a simplification to make it easer to track how many folks
                there are without having to sum up all the stocks.
    """
    return 1000


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Day
    The final time for the simulation.
    """
    return 100


@cache('step')
def recovering():
    """
    Recovering
    ----------
    (recovering)
    Persons/Day

    """
    return infectious() / duration()


@cache('step')
def susceptible():
    """
    Susceptible
    -----------
    (susceptible)
    Persons
    The population that has not yet been infected.
    """
    return _state['susceptible']


def _init_recovered():
    """
    Implicit
    --------
    (_init_recovered)
    See docs for recovered
    Provides initial conditions for recovered function
    """
    return 0


def _init_infectious():
    """
    Implicit
    --------
    (_init_infectious)
    See docs for infectious
    Provides initial conditions for infectious function
    """
    return 5


@cache('run')
def contact_infectivity():
    """
    Contact Infectivity
    -------------------
    (contact_infectivity)
    Persons/Persons/Day
    A joint parameter listing both how many people you contact, and how likely
                you are to give them the disease.
    """
    return 0.3


@cache('step')
def infectious():
    """
    Infectious
    ----------
    (infectious)
    Persons
    The population with the disease, manifesting symptoms, and able to
                transmit it to other people.
    """
    return _state['infectious']


@cache('step')
def _drecovered_dt():
    """
    Implicit
    --------
    (_drecovered_dt)
    See docs for recovered
    Provides derivative for recovered function
    """
    return recovering()


@cache('step')
def _dinfectious_dt():
    """
    Implicit
    --------
    (_dinfectious_dt)
    See docs for infectious
    Provides derivative for infectious function
    """
    return succumbing() - recovering()


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Day [0,?]
    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Day
    The initial time for the simulation.
    """
    return 0


def _init_susceptible():
    """
    Implicit
    --------
    (_init_susceptible)
    See docs for susceptible
    Provides initial conditions for susceptible function
    """
    return total_population()


@cache('step')
def time():
    """
    TIME
    ----
    (time)
    None
    The time of the model
    """
    return _t


@cache('run')
def duration():
    """
    Duration
    --------
    (duration)
    Days
    How long are you infectious for?
    """
    return 5


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Day [0,?]
    The time step for the simulation.
    """
    return 0.03125


@cache('step')
def _dsusceptible_dt():
    """
    Implicit
    --------
    (_dsusceptible_dt)
    See docs for susceptible
    Provides derivative for susceptible function
    """
    return -succumbing()


@cache('step')
def succumbing():
    """
    Succumbing
    ----------
    (succumbing)
    Persons/Day

    """
    return susceptible() * infectious() / total_population() * contact_infectivity()


@cache('step')
def recovered():
    """
    Recovered
    ---------
    (recovered)
    Persons
    These people have recovered from the disease. Yay! Nobody dies in this
                model.
    """
    return _state['recovered']


def time():
    return _t
functions.time = time
functions.initial_time = initial_time
