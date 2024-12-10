import pytest

@pytest.fixture()
def fixtureMethod():
    print("This is a fixture method")
    return None  # Return None to make it a valid fixture

def test_methodA(fixtureMethod):
    print("This is a method A")

def test_methodB(fixtureMethod):
    print("This is a method B")

def test_methodC(fixtureMethod):
    print("This is a method C")

def test_methodD(fixtureMethod):
    print("This is a method D")