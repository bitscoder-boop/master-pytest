from greeting import my_name
import pytest

@pytest.fixture
def bob():
    return "My name is: bob"


@pytest.fixture
def sally():
    return "My name is: sally"


def test_my_name():
    assert "My name is: Dipesh" == my_name("Dipesh")


def test_bob(bob):
    assert bob == my_name("bob")


def test_sally(sally):
    assert sally == my_name("sally")
