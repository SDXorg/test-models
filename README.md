# test-models
A collection of models implemented in various environments with a canonical output

Each directory should contain:
- one model concept, with a single canonical output named `output.csv` containing (at least) the stock values over the standard timeseries in the model files
- Model files that produce said output (.mdl, .xmile, stella, pysd, etc)
- A text file containing:
 - The purpose of the test model (what functionality it executes)
 - The version of software that the canonical output was originally prepared by
 - The author of the test model and contact info
 - Submission Date
- Screenshots of model construction programs (optional)

For a demonstration, see the [teacup example](https://github.com/SDXorg/test-models/tree/master/teacup)
