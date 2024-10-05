from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import get_books_info, get_category_links
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
url = "https://books.toscrape.com"
driver.get(url)
time.sleep(2)

categories = driver.find_elements(By.XPATH, "//div[@class = 'side_categories']/ul/li/ul/li/a")
Travel = categories[0]

# Get links for the Travel category
travel_links = get_category_links(driver, Travel)

# Navigate back to the main page
driver.get(url)
time.sleep(2)

# Re-fetch the categories after navigating back
categories = driver.find_elements(By.XPATH, "//div[@class = 'side_categories']/ul/li/ul/li/a")
Nonfiction = categories[11]

# Get links for the Nonfiction category
nonfiction_links = get_category_links(driver, Nonfiction)

# Combine the links from both categories
links = travel_links + nonfiction_links
print(len(links))

df = get_books_info(links)
df = df.reset_index(drop=True)
df['id'] = range(1, len(df) + 1)

# Set 'id' as the index and name the index column
df = df.set_index('id').rename_axis('ID')
print(df)

df.to_csv("Books.csv")
driver.quit()