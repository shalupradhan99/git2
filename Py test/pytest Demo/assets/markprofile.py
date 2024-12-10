import pytest

@pytest.mark.profile
def test_smoke_testing():
    print("This is smoke testing")

@pytest.mark.profile
def test_sanity_testing():
    print("This is sanity testing")

def test_end_to_end_testing():
    print("This is end-to-end testing")

def test_regression_testing():
    print("This is regression testing")