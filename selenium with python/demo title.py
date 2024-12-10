from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the path to your ChromeDriver if necessary
driver.maximize_window()
# Open the Holland & Barrett login page
#driver.get("https://demo.opencart.com/")
#driver.get("https://www.freecrm.com/en")
driver.get("https://www.ebay.com/")
driver.minimize_window()
time.sleep(6)

driver.maximize_window()
time.sleep(5)
# Wait for the page to load
# Get and verify the title of the page
expected_title = "Login - Holland & Barrett"  # Replace with the correct expected title
actual_title = driver.title

if actual_title == expected_title:
    print("Login is successful . . . . . Well done Python ")
else:
    print("Login Unsuccessful . . . . . Very good my boy")

# Close the driver after use
driver.quit()