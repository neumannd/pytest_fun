[![Build Status](https://travis-ci.org/neumannd/pytest_fun.svg?branch=master)](https://travis-ci.org/neumannd/pytest_fun)

# Introduction

This GitHub repository is meant for collecting `pytest` example code to introduce colleagues to `pytest`.

Pytest is a python based testing framework, which is used to write and execute test code. You can write code to test anything like database , API. But in the industry pytest is mainly used to write tests for APIs. 

# Advantages

* Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
* Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
* Pytest allows us to skip a subset of the tests during execution.
* Pytest allows us to run a subset of the entire test suite.
* Pytest is free and open source.
* Because of its simple syntax, pytest is very easy to start with
* Pytest  can  be  used  with  most  existing  test  suites, like nosetest, python unittest, doctest

# Installation

Get sources from GitHub:

```
$ git clone https://github.com/neumannd/pytest_fun.git
$ cd pytest_fun
```

You can use a [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) environment with Python 3.8:

```
$ conda create -n pytest_fun python=3.8 pytest numpy
$ conda activate pytest_fun
```

Run the installation:
```
$ python setup.py develop
```

# Run tests

Run all tests with pytest:
```
$ pytest
```
This will run all the filenames starting with test_ and the filenames ending with _test in that folder and subfolders under that folder. 

To run tests only from a specific file, we can use:
```
$ pytest tests\test_simple.py
```
# Pytest command line options

```
$ pytest -x           # stop after first failure
$ pytest --maxfail=2  # stop after two failures
$ pytest -v           # verbose
```
see also: https://gist.github.com/kwmiebach/3fd49612ef7a52b5ce3a

# Create an html output

Add pytest-html to conda environment:
```
$ conda install pytest-html
```
Run pytest and create html output:
```
$ pytest --html=report.html
```
# conftest.py: sharing fixture functions

If during implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a conftest.py file. You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. The discovery of fixture functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins.

# Reading material

* https://docs.pytest.org/en/latest/
* https://www.tutorialspoint.com/pytest/pytest_tutorial.pdf

# Examples for projects using pytest

## IOOS Compliance Checker

* url: https://github.com/ioos/compliance-checker
* tests directory: [compliance_checker/tests](https://github.com/ioos/compliance-checker/tree/master/compliance_checker/tests)
* one testing file per module
* pytest decorators: does only use marks
* see `pytest.ini` in root directory for usage of some possible control parameters


# Contributors:

* @am-kaiser
* @MacPingu
* @neumannd
