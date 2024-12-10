import time
from selenium import webdriver
import unittest
from LoginPageandAddtocart1 import LoginPageandAddtocart1
class LoginTests(unittest.TestCase):
    def test_validLogin(self):
        baseUrl = "https://auth.hollandandbarrett.com/u/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)
        lp = LoginPageandAddtocart1(driver)
        lp.login("shyam143pr@gmail.com","Sam@pr9493!")