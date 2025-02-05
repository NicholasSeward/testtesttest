# File: tests/test_main.py

import pytest
from main import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_positive_and_negative():
    assert add(5, -3) == 2


def test_add_with_zero():
    assert add(0, 4) == 4


def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
