import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Step:1
#Open the website
class LoginPageandAddtocart1():
    def __init__(self,driver):
        self.driver = driver
        self.driver.save_screenshot(".//driver.png")
    #Locators
    _email_field ="username"
    _password_field="password"
    _login_button ="//button[normalize-space()='Sign In']"
    _vitamin_btn="//button[normalize-space()='Vitamins']"
    _veganChocolate_btn="//button[normalize-space()='Vegan Chocolate']"
    _vitaminC_btn ="//div[normalize-space()='Vitamin C']"
    _Home_btn="//a[normalize-space()='Home']"
#Step:2
#Login with the registered user
    def getEmailFeild(self):
        return self.driver.find_element(By.ID,self._email_field)
    def getPasswordField(self):
        return self.driver.find_element(By.NAME,self._password_field)
    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)
#Step:3
# Add any Vitamin C products from 'Vitamins & Supplements' to the basket
    def get(self):
        self.driver.get("https://auth.hollandandbarrett.com/")
        time.sleep(4)
    def getVitaminandSupplements(self):
        partial_link = "Vitamins"
        self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link).click()
    def getVitamins(self):
        return self.driver.find_element(By.XPATH, self._vitamin_btn)
    def getVitaminC(self):
        return self.driver.find_element(By.XPATH, self._vitaminC_btn)
#Step:4
#Add any Vegan Chocolate products from 'Vegan' to the basket
    def ClickHome(self):
        return self.driver.find_element(By.XPATH,self._Home_btn)
    def getVegan(self):
        partial_link = "Vegan"
        self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link).click()
    def getVeganChocolate(self):
        return self.driver.find_element(By.XPATH,self._veganChocolate_btn)
    def enterEmail(self,email):
        self.getEmailFeild().send_keys(email)
    def enterPassword(self,password):
        self.getPasswordField().send_keys(password)
    def clickLoginButton(self):
        self.getLoginButton().click()
    def Clickvitamins(self):
        self.getVitamins().click()
    def clickvitaminC(self):
        self.getVitaminC().click()
    def AddItemsVitaminC(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"button-ProductCard\"]").click()
        time.sleep(3)
    def ClickHm(self):
        self.ClickHome().click()
    def clickvgchoc(self):
        self.getVeganChocolate().click()
        time.sleep(3)
    def AddVeganItems(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"button-ProductCard\"]").click()
        time.sleep(3)
#Step:5
#Verify both the products are added to the basket
    def ClickMyB(self):
        self.driver.find_element(By.CSS_SELECTOR, ".HeaderLinkIcon-module_button__C7r3R svg").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
        time.sleep(3)
    def login(self,email,password,):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.driver.save_screenshot(".//clickLoginButton.png")
        self.get()
        self.getVitaminandSupplements()
        self.Clickvitamins()
        self.clickvitaminC()
        self.AddItemsVitaminC()
        self.driver.save_screenshot(".//AddItemsVitaminC.png")
        self.ClickHm()
        self.getVegan()
        self.clickvgchoc()
        self.AddVeganItems()
        self.driver.save_screenshot(".//AddVeganItems.png")
        self.ClickMyB()
        self.driver.save_screenshot(".//ClickMyB.png")