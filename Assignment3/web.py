# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.flipkart.com")
time.sleep(5)

# Selecting to close the login pop-up page
close_link = driver.find_element("xpath","/html/body/div[3]/div/span")

close_link.click()

time.sleep(5)

# Selecting fashion tab
fashion_link = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/a[5]/div/div/div/div/img")

fashion_link.click()

time.sleep(5)


# Selecting favourite shoe tab
shoe_link = driver.find_element("xpath","/html/body/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/a/div[1]/div/img")

shoe_link.click()

time.sleep(5)

# Selecting sorting shoe price from "high to low" tab
price_link = driver.find_element("xpath","/html/body/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[3]")

price_link.click()

time.sleep(5)

# Selecting brand tab
brand_link = driver.find_element("xpath","/html/body/div/div/div[3]/div/div[1]/div/div/div/section[5]/div[2]/div[1]/div[3]/div/label/div[1]")

brand_link.click()

time.sleep(5)

# Finding the search bar and entering texts

search_bar = driver.find_element("xpath","/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search_bar.send_keys("nike")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)


# Selecting a nike shoes from the search results
nike_link = driver.find_element("xpath","/html/body/div/div/div[3]/div[1]/div[2]/div[3]/div/div[2]/div/div/a[1]")

nike_link.click()



# Waiting for the laptop details page to load
time.sleep(5)



# Closing the webdriver
driver.close()