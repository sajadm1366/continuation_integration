from main import add_fucntion, multiply_function


def test_add():
    assert 2 == add_fucntion(1, 1)


def test_multiply():
    assert 10 == multiply_function(2, 5)