import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch the browser and open the URL
driver = webdriver.Chrome()  # Update path to your ChromeDriver
driver.get("https://www.easycalculation.com/")  # URL of the website
driver.maximize_window()
time.sleep(3)  # Allow the page to load completely


links = driver.find_elements(By.TAG_NAME, "a")  # Locate all <a> tags (links)
print(f"Number of links on the page: {len(links)}")

    # Step 3: Click on the "Love Calculator" link
for link in links:
        if "Love Calculator" in link.text:  # Match the link's text
            print("Clicking on Love Calculator link...")
            link.click()
            break
        else:
            print("Love Calculator link not found.")

time.sleep(3)  # Pause to observ:
    # Step 4: Close the browser
driver.quit()

