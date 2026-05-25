from scr.app import add_two_numbers


def test_add_two_numbers_with_positive_integers():
    assert add_two_numbers(2, 3) == 5


def test_add_two_numbers_with_negative_and_positive():
    assert add_two_numbers(-1, 4) == 3


def test_add_two_numbers_with_zero():
    assert add_two_numbers(0, 0) == 0
