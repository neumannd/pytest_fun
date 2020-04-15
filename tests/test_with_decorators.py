from pytest_fun.funs import add
import pytest


# see for details:
#   * https://docs.pytest.org/en/latest/parametrize.html
#   * https://docs.pytest.org/en/latest/example/parametrize.html#paramexamples


# ~~~~ test for equality ~~~~
@pytest.mark.use_parameterize
@pytest.mark.parametrize("input_args,expected",
                         [([3, 2], 5),
                          ([3, 1], 4),
                          ([55, 3], 58),
                          ([107, 243], 350)])
def test_add_true(input_args, expected):
    assert add(input_args[0], input_args[1]) == expected


# ~~~~ mark a still-failing test ~~~~
@pytest.mark.use_parameterize
@pytest.mark.parametrize("input_args,expected",
                         [([3, 2], 5),
                          ([3, 1], 4),
                          pytest.param([2, 2], 3, marks=pytest.mark.xfail)])
def test_add_true(input_args, expected):
    assert add(input_args[0], input_args[1]) == expected


# ~~~~ test for inequality ~~~~
@pytest.mark.use_parameterize
@pytest.mark.parametrize("input_args,expected",
                         [([3, 2], 4),
                          ([3, 1], 2),
                          ([55, 3], 57),
                          ([107, 243], 300),
                          pytest.param([2, 2], 4, marks=pytest.mark.xfail),
                          pytest.param([2, 2], 3, marks=pytest.mark.xfail)])
def test_add_false(input_args, expected):
    assert add(input_args[0], input_args[1]) != expected


# ~~~~ test different permutations of input arguments ~~~~
@pytest.mark.use_parameterize
@pytest.mark.parametrize("a", [0, 1, 2, 3, 103])
@pytest.mark.parametrize("b", [2, 3, 5, 10, 24, 105, 212])
def test_add_permutated(a, b):
    assert add(a, b) == a+b
    assert add(a, b) != a+b+1
    assert add(a, b) != a+b-1


# ~~~~ give names to the tests by parameterize ~~~~
@pytest.mark.use_parameterize
@pytest.mark.parametrize("input_args,expected",
                         [([3, 2], 5),
                          ([107, 243], 350),
                          ([2.3, 2.1], 4.4)],
                         ids=['small int', 'large int', 'float'])
def test_add_with_ids(input_args, expected):
    assert add(input_args[0], input_args[1]) == expected
