import pytest


@pytest.fixture()
def setup():
    print("i will be excecuting when fixture will call")
    yield
    print("i will execute last")

@pytest.fixture
def setup_data():
    data = {"key1": "value1", "key2": "value2"}
    print("Setup data fixture")
    return data