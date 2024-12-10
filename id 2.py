from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Holland & Barrett login page
driver.get("https://auth.hollandandbarrett.com/u/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("shalupradhan99@gmail.com")
username.send_keys(Keys.RETURN)
time.sleep(5)

password = driver.find_element(By.NAME, "password")
password.send_keys("GdSJhj*b.nL6gSN")
# edit_box.send_keys(Keys.RETURN)
time.sleep(5)

# edit_box = driver.find_element(By.XPATH, '//button[@class="c12f661b1 c567de7a4 c09c9561d c8b873213 c428cfe12"]')
signin = driver.find_element(By.NAME, "action").click()
time.sleep(3)
print("Test successful")


