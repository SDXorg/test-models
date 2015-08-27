Models for testing system dynamics translation, simulation, and display software
================================================================================

This repository hopes to be a resource for testing system dynamics software and translation tools
by providing a standard set of simple test cases in various formats, with an agreed upon canonical 
output. 

Folders within the [Test](https://github.com/SDXorg/test-models/tree/master/tests/) directory 
contain models that exercise a specific component of the system dynamics modeling paradigm, 
in a number of different vendor or software formats.

Folders within the [Benchmarks](https://github.com/SDXorg/test-models/tree/master/benchmarks/) 
directory contain models that can be used for evaluating and comparing the execution speed of 
each software platform version.

Folders within the [Benchmarks](https://github.com/SDXorg/test-models/tree/master/examples/) 
directory contain models that are standard formulations in the SD field that may exhibit more 
complexity than test models.

Each model folder contains:
- a single model concept, with its canonical output (named `output.csv`) containing (at least) 
the stock values over the standard timeseries in the model files
- Model files that produce said output (.mdl, .xmile, stella, pysd, etc)
- A text file entitled `README.md` containing:
 - The purpose of the test model (what functionality it executes)
 - The version of software that the canonical output was originally prepared by
 - The author of the test model and contact info
 - Submission Date
- Screenshots of model construction programs (optional)

For a demonstration, see the 
[teacup example](https://github.com/SDXorg/test-models/tree/master/example/teacup)


## Tests to Add:
- Delays and Smoothing Functions
- Trig Functions
- Logical Functions

