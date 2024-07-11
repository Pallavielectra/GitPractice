import pytest


def test_firstprogram(setup):
    print("Hello")


@pytest.mark.skip
def test_secondprogram():
    print("Good Morning")