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
* Pytest  can  be  used  with  most  existing  test  suites, like nosetest, python unittest, doctest.

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
$ pytest -m use_fixtures # run only specific tests marked with the tag
                         # `use_fixtures` (details below in "pytest markers")
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

# pytest markers

We can use pytest **markers** to select only a subset of tests to run. This is useful if some tests only work in specific environments (with database access; unter certain operation systems). Markers are defined in the `pytest.ini` file. Then, functions can be individually marked with them.

Example for definition of markers in `pytest.ini`:

```
markers =
        use_fixtures: tests are performed in which pytest.fixtures are used
        use_parameterize: tests are performed in which pytest.mark.parameterize is used
        skipped_and_xfailing_tests: test that are marked to be skipped or marked to fail (`xfail`)
```

Example for marking a functions with a marker:

``` python
@pytest.mark.use_fixtures
def test_write_int_to_file():
    # define a temporary directory
    tmpdir = Path('/tmp')

    file_path = tmpdir / 'my_file.txt'
    write_int_to_file(5, file_path)
    assert file_path.read_text() == '5'
```

To performed only tests marked by marked `use_fixtures` (example) do:

``` bash
pytest -m use_fixtures
```

To perform all tests except those marked by `use_fixtures` (example) do:

``` bash
pytest -m "not use_fixtures"
```


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


# Further Reading

## Using mock modules

Sometimes you have a database or an external service which is not available for your test environment.
In theses cases you can use mock modules to fake the responses of the database/service to return an expected value.
The database/service don't need to be available to run the test code.

* https://docs.pytest.org/en/latest/monkeypatch.html
* https://docs.python.org/dev/library/unittest.mock.html

# Contributors:

* @am-kaiser
* @MacPingu
* @neumannd
