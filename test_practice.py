import pytest


def function(X):
    return X + 5


@pytest.mark.smoke
def test_Methond():
    assert function(3) == 8
