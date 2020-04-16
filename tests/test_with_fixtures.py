from pytest_fun.funs import write_int_to_file, sum_dict
import pytest
from pathlib import Path


# ~~~~ test write_int_to_file ~~~~
@pytest.mark.use_fixtures
def test_write_int_to_file():
    # define a temporary directory
    tmpdir = Path('/tmp')

    file_path = tmpdir / 'my_file.txt'
    write_int_to_file(5, file_path)
    assert file_path.read_text() == '5'

    # ~ uncomment the last line to see the output of the `print` command
    # print(tmpdir)
    # assert False


# ~~~~ get a temporary directory for our data ~~~~
# Use case: we need a tmp directory to do some things in there. We could
#           create our own tmp directory, do the things and, in the end,
#           remove it. Pytest offers a functionality that provides such a
#           directory. We just provide `tmpdir` to the call of the test
#           function.
#           This `tmpdir` is a so-called `fixture`. Fixtures are functions
#           that are implicitely called when used as argument in a function
#           call. Fixtures are meant to generate input data for testing
#           functions.
#           Details for the `tmpdir` fixture are provided here:
#    https://docs.pytest.org/en/latest/reference.html#std:fixture-tmpdir
#           A list of all available fixtures is provided here:
#             https://docs.pytest.org/en/latest/fixture.html
@pytest.mark.use_fixtures
def test_write_int_to_file_with_fixture(tmpdir):
    file_path = Path(str(tmpdir)) / 'my_file.txt'
    write_int_to_file(5, file_path)
    assert file_path.read_text() == '5'

    # ~ uncomment the last line to see the output of the `print` command
    # print(tmpdir)
    # assert False


# ~~~~ test output stream ~~~~
#  see for details:
#   https://docs.pytest.org/en/latest/reference.html#std:fixture-capfd
@pytest.mark.use_fixtures
def test_output(capfd):
    print('Hello World!')
    captured = capfd.readouterr()
    assert captured.out == 'Hello World!\n'


# ~~~~ test sum_dict ... using our own fixture ~~~~
# Instead of using existing fixtures, we can also make our own ones.
#
# We want to test the function `sum_dict`. For this purpose we need a
# dictionary. Hence, we will create a fixture that creates us a dictionary.
#
# Define fixture
@pytest.fixture
def input_dict():
    input = {'a': 1, 'b': 2, 'c': 3}
    return input


# use the fixture
@pytest.mark.use_fixtures
def test_sum_dict(input_dict):
    assert sum_dict(input_dict) == sum(input_dict.values())

    # ~ uncomment the last line to see the output of the `print` commands
    # print(type(input_dict))
    # print(input_dict)
    # assert False
