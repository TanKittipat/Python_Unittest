from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Initialize the Chrome WebDriver
s = Service('D:\webdriver\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open Google
driver.get("https://www.yahoo.com/")

# Find the search box element and enter a query
search_box = driver.find_element(By.XPATH,'//*[@id="ybar-sbq"]')
search_box.send_keys("npru")

# Perform the search
# search_box.send_keys(Keys.RETURN)
btn = driver.find_element(By.XPATH,'//*[@id="ybar-search"]')
btn.click()
# Wait for the search results to load
time.sleep(5)

# Print the title of the current page
print(driver.title)

# Close the browser
driver.quit()