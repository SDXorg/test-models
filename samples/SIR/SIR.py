"""
Python model test-models/samples/SIR/SIR.py
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
    'Contact Infectivity': 'contact_infectivity',
    'Duration': 'duration',
    'Infectious': 'infectious',
    'Recovered': 'recovered',
    'Recovering': 'recovering',
    'Succumbing': 'succumbing',
    'Susceptible': 'susceptible',
    'Total Population': 'total_population',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'}


@cache('run')
def contact_infectivity():
    """
    Contact Infectivity

    Persons/Persons/Day

    A joint parameter listing both how many people you contact, and how likely 
        you are to give them the disease.
    """
    return 0.3


@cache('run')
def duration():
    """
    Duration

    Days

    How long are you infectious for?
    """
    return 5


@cache('step')
def infectious():
    """
    Infectious

    Persons

    The population with the disease, manifesting symptoms, and able to 
        transmit it to other people.
    """
    return integ_infectious()


@cache('step')
def recovered():
    """
    Recovered

    Persons

    These people have recovered from the disease. Yay! Nobody dies in this 
        model.
    """
    return integ_recovered()


@cache('step')
def recovering():
    """
    Recovering

    Persons/Day


    """
    return infectious() / duration()


@cache('step')
def succumbing():
    """
    Succumbing

    Persons/Day


    """
    return susceptible() * infectious() / total_population() * contact_infectivity()


@cache('step')
def susceptible():
    """
    Susceptible

    Persons

    The population that has not yet been infected.
    """
    return integ_susceptible()


@cache('run')
def total_population():
    """
    Total Population

    Persons

    This is just a simplification to make it easer to track how many folks 
        there are without having to sum up all the stocks.
    """
    return 1000


@cache('run')
def final_time():
    """
    FINAL TIME

    Day

    The final time for the simulation.
    """
    return 100


@cache('run')
def initial_time():
    """
    INITIAL TIME

    Day

    The initial time for the simulation.
    """
    return 0


@cache('step')
def saveper():
    """
    SAVEPER

    Day [0,?]

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    TIME STEP

    Day [0,?]

    The time step for the simulation.
    """
    return 0.03125


integ_infectious = functions.Integ(lambda: succumbing() - recovering(), lambda: 5)

integ_recovered = functions.Integ(lambda: recovering(), lambda: 0)

integ_susceptible = functions.Integ(lambda: -succumbing(), lambda: total_population())
