import pytest


@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "This test case failed beacuse string are not match"


def test_secondProgram(setup):
    a = 2
    b = 3
    assert a+3 == 5




