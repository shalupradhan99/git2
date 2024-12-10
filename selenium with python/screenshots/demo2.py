#1. Open using any Browser
		#a.	Chrome Browser
		#b.	Firefox
		#c.	Edge Enter values using Locator ID
#2.Open URL:https://www.easycalculation.com/
	#3.Print Page Title
	#4.Get page Source and Page Source length
	#5.Close the Browser
    # 6.Take Screenshots on every steps


from selenium import webdriver



# For Firefox
driver = webdriver.Firefox()

# Step 2: Open URL
url = "https://www.easycalculation.com/"
driver.get(url)
driver.save_screenshot('.//FirstSteps1.png')
# Step 3: Get Page Title name and Title length
title = driver.title
title_length = len(title)

# Step 4: Print Page Title and Title length on the Console
print(f"Page Title: {title}")
print(f"Title Length: {title_length}")

# Step 5: Get page URL and verify whether it is the desired page or not
current_url = driver.current_url
if current_url == url:
    print("URL Verified: The URL is correct.")
else:
    print("URL Verification Failed: Incorrect URL.")

# Step 6: Get page Source and Page Source length
page_source = driver.page_source
page_source_length = len(page_source)
driver.save_screenshot('.//Third Steps1.png')

# Step 7: Print Page Source length on Console
print(f"Page Source Length: {page_source_length}")

# Step 9: Close the Browser
driver.quit()