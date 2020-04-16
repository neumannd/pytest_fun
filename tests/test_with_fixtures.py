from pytest_fun.funs import write_int_to_file, sum_dict
import pytest
from pathlib import Path


# ~~~~ test write_int_to_file ~~~~
@pytest.mark.io_tests
def test_write_int_to_file():
    # define a temporary directory
    tmpdir = Path('/tmp')

    file_path = tmpdir / 'my_file.txt'
    write_int_to_file(5, file_path)
    assert file_path.read_text() == '5'

    # ~ uncomment the last line to see the output of the `print` command
    # print(tmpdir)
    # assert False


# ~~~~ test write_int_to_file with external definition of tmp directory ~~~~
# We need a tmp directory to do some things in there. We do not want to set
# the tmp directory manually, but want to get it from `somewhere`. A decorator
# could be used for this purpose. Pytest provides a functionality called
# `fixture` that is a bit simpler to use and to set up.
# 
# Fixtures are functions that are implicitely called when used as argument in
# a function header. NOTE: The fixture is not passed as argument value when the
# function is called but as argument name in the function definition. Fixtures
# are meant to generate input data, to prepare something or do some more 
# advanced stuff for testing functions.
#
# Define fixture
@pytest.fixture
def get_tmpdir():
    tmpdir = Path('/tmp')
    return tmpdir

# use the fixture
@pytest.mark.use_fixtures
@pytest.mark.io_tests
def test_write_int_to_file_with_own_fixture(get_tmpdir):
    file_path = get_tmpdir / 'my_file.txt'
    write_int_to_file(5, file_path)
    assert file_path.read_text() == '5'


# ~~~~ test write_int_to_file using a predefined fixture ~~~~
# We use the predefined fixture `tmpdir` that provides us a temporary
# directory. The nice thing is that we do not have to think about the
# location of the tmp directory (i.e. for different operating systems).
# Details for the `tmpdir` fixture are provided here:
#    https://docs.pytest.org/en/latest/reference.html#std:fixture-tmpdir
# A list of all available fixtures is provided here:
#    https://docs.pytest.org/en/latest/fixture.html
@pytest.mark.use_fixtures
@pytest.mark.io_tests
def test_write_int_to_file_with_predefined_fixture(tmpdir):
    # `tmpdir` is alreay a `Path` object but it caused strange errors.
    # Therefore, we do the `Path(str(...))`.
    file_path = Path(str(tmpdir)) / 'my_file.txt'
    write_int_to_file(5, file_path)
    assert file_path.read_text() == '5'

    # ~ uncomment the last line to see the output of the `print` command
    # print(tmpdir)
    # assert False


# ~~~~ test output stream ~~~~
# The `capfd` fixture captures the output and error streams. Thus, the command
# line output of programms can be tested. For details on `capfd` see:
#    https://docs.pytest.org/en/latest/reference.html#std:fixture-capfd
@pytest.mark.use_fixtures
@pytest.mark.io_tests
def test_output(capfd):
    print('Hello World!')
    captured = capfd.readouterr()
    assert captured.out == 'Hello World!\n'


# ~~~~ test sum_dict ... using our own fixture ~~~~
# Another example with a self-made fixture
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
