import pytest


def test_FixtureDemo(setup):
    print("I will be executing steps in fixtureDemo method")



# Use the fixture in a test
def test_example(setup_data):
    assert setup_data["key1"] == "value1"
    assert setup_data["key2"] == "value2"