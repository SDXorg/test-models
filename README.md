Models for testing system dynamics translation, simulation, and display software
================================================================================

This repository is a resource for testing system dynamics software and translation tools.
It provides a standard set of simple test cases in various formats, with a proposed canonical 
output for that test. 

Folders within the [Test](https://github.com/SDXorg/test-models/tree/master/tests/) directory 
contain models that exercise a specific component of the system dynamics modeling paradigm, 
in a number of different vendor or software formats.

Folders within the [Benchmarks](https://github.com/SDXorg/test-models/tree/master/benchmarks/) 
directory contain models that can be used for evaluating and comparing the execution speed of 
each software platform version, have more complexity than the simple unit test style examples above.

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
[teacup example](https://github.com/SDXorg/test-models/tree/master/benchmarks/teacup)


## Contributing:
All members of the SD community are invited to contribute to this repository. To do so, create a 
local clone, add your contribution using one of the following methods, add yourself to the
[AUTHORS](AUTHORS) file, then submit a pull request. 

To request that a specific test be added, create an issue on the 
[issues](https://github.com/SDXorg/test-models/issues) page of this repository.

#### Expanding existing cases
Many of these cases have model files for some modeling formats but not others. To add a model file
in another format, check that your model output replicates the 'canonical example' to reasonable 
fidelity, preferably using identical varaibale names, and add an entry to the contributions table
in the directory's `README.md` file.

#### Adding new cases
To add a new case, in your local clone add a folder in either the `tests` or `benchmarks` directory
as appropriate, copy an example `README.md` file from another folder, and edit to suit your needs.




