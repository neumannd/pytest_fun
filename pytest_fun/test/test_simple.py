from pytest_fun.funs import add, sub, square


def test_add():
    assert add(1, 1) == 2
    assert add(3, 2) == 5
    assert add(2, 3) == 5
    assert add(2.5, 3.3) == 5.8


def test_sub():
    assert sub(1, 1) == 0
    assert sub(5, 4) == 1
    assert sub(4, 5) == -1


def test_square():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
