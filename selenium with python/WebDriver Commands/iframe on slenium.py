from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH or specify its full path
driver.maximize_window()

# Load the local HTML file
driver.get("file:///C:/Users/shalu/Downloads/frame.html")
time.sleep(2)

# Switch to the first frame and login to Holland & Barrett
driver.switch_to.frame("HollandandBarrett")
driver.get("https://auth.hollandandbarrett.com/u/login")
time.sleep(2)

driver.find_element(By.ID, value='username').send_keys("ridhishapradhan19@gmail.com")
driver.find_element(By.NAME, value='password').send_keys("Momdad@506")
driver.find_element(By.XPATH, value="/html/body/main/section/div/div/div/form/div[2]/button").click()
time.sleep(5)

# Switch back to the main page
driver.switch_to.default_content()
driver.get("file:///C:/Users/shalu/Downloads/frame.html")
time.sleep(2)

# Navigate to Selenium website
driver.get("https://www.selenium.dev/")
time.sleep(2)
driver.find_element(By.XPATH, value="//*[@id='main_navbar']/ul/li[2]/a/span").click()
time.sleep(5)

# Return to the main page and interact with another frame for OpenCart
driver.get("file:///C:/Users/shalu/Downloads/frame.html")
time.sleep(2)

# Switch to the "my store" frame and navigate to OpenCart
driver.switch_to.frame("my store")
driver.get("https://demo.opencart.com/")  # Ensure the URL is correct
time.sleep(5)

# Interact with the search box and perform a search
driver.find_element(By.NAME, value="search").send_keys("product")
driver.find_element(By.NAME, value="search").send_keys(Keys.RETURN)
time.sleep(5)

# Close the browser
driver.quit()
