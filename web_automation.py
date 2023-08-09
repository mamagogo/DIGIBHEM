from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Define URL and create WebDriver object
url = "https://www.google.com"
driver = webdriver.Chrome()  # Use the appropriate driver for your browser
driver.get(url)

# Automate search functionality
search_input = driver.find_element_by_name("q")  # Corrected method name
search_input.send_keys("automation testing with Selenium")
search_input.send_keys(Keys.RETURN)

# Verify search results
time.sleep(2)  # Wait for the results to load (you might need to adjust this)
search_results = driver.find_elements_by_css_selector(".tF2Cxc")  # CSS selector for search results
assert len(search_results) > 0, "No search results found"

# Close the browser
driver.quit()
