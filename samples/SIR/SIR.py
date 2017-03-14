"""
Python model test-models/samples/SIR/SIR.py
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
    'Duration': 'duration',
    'Succumbing': 'succumbing',
    'Time': 'time',
    'TIME': 'time',
    'Susceptible': 'susceptible',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'Contact Infectivity': 'contact_infectivity',
    'FINAL TIME': 'final_time',
    'TIME STEP': 'time_step',
    'Total Population': 'total_population',
    'Recovering': 'recovering',
    'Infectious': 'infectious',
    'Recovered': 'recovered'
}


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
    return integ_infectious()


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


integ_recovered = functions.Integ(lambda: recovering(), lambda: 0)


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
def recovered():
    """
    Recovered
    ---------
    (recovered)
    Persons
    These people have recovered from the disease. Yay! Nobody dies in this 
        model.
    """
    return integ_recovered()


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


integ_infectious = functions.Integ(lambda: succumbing() - recovering(), lambda: 5)


@cache('step')
def susceptible():
    """
    Susceptible
    -----------
    (susceptible)
    Persons
    The population that has not yet been infected.
    """
    return integ_susceptible()


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
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Day
    The final time for the simulation.
    """
    return 100


integ_susceptible = functions.Integ(lambda: -succumbing(), lambda: total_population())


@cache('step')
def succumbing():
    """
    Succumbing
    ----------
    (succumbing)
    Persons/Day

    """
    return susceptible() * infectious() / total_population() * contact_infectivity()


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
