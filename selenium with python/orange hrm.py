

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Launch a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#driver.get("https://demo.opencart.com/")
#driver.get("https://in.pinterest.com/pin/1037024251694490295/")
# Maximize the browser window
driver.maximize_window()
time.sleep(5)  # Wait for a while to observe the browser maximized

# Verify the title of the browser
title = driver.title
print("Browser Title (after maximization):", title)
# Assert that the title contains "Google"

# Minimize the browser window
driver.minimize_window()
time.sleep(5)  # Wait for a while to observe the browser minimized

# Verify the title again
title = driver.title
print("Browser Title (after minimization):", title)
 # Assert that the title contains "Google"

# Close the browser
driver.quit()
