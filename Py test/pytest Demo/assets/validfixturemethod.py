import pytest

@pytest.fixture()
def loginapplication():
    print("This is a fixture method")
    return None  # Return None to make it a valid fixture

def test_searchingtheproduct(loginapplication):
    print("Searching the Products")


@pytest.mark.skip
def test_AddItemToCart(loginapplication):
    print("Adding items to the Cart")

def test_CheckingAddItemInCart(loginapplication):
    print("These are Checking Items added in Cart ")

@pytest.mark.xfail
def test_PaymentDetails(loginapplication):
    print("These are PaymentDetails")