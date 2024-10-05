from bs4 import BeautifulSoup
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time
from selenium.webdriver.common.by import By

def get_books(driver):
    xpath = "//li[@class = 'col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/h3/a[@href]"
    booklinks = driver.find_elements(By.XPATH, f"{xpath}")
    links = [book.get_attribute("href") for book in booklinks]
    for link in links:
        print(link)
        print("---------------")
    return links

def fetch_book_info(book_url):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find("h1").text
    price = soup.find("p", class_="price_color").text
    star = soup.find("p", {"class": "star-rating"})["class"][1]
    product_description_tag = soup.find("p", class_="")
    product_description = product_description_tag.text if product_description_tag else "No description available"
    table_rows = soup.find_all("tr")

    book_info = {
        "Title": title,
        "Price": price,
        "Star Rating": star,
        "Product Description": product_description
    }

    list_of_last_4 = ["UPC", "Product Type", "Price (excl. tax)", "Price (incl. tax)", "Tax", "Availability", "Number of reviews"]
    for i, row in enumerate(table_rows):
        book_info[list_of_last_4[i]] = row.find("td").text

    return book_info

def get_books_info(links):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_book_info, links))
    return pd.DataFrame(results)

def get_category_links(driver, category_element):
    category_element.click()
    time.sleep(2)
    category_url = driver.current_url
    category_links = []

    # Modify the URL to navigate through pages
    base_category_url = category_url.replace("index.html", "page-{}.html")

    for i in range(1, 999):
        if i == 1:
            driver.get(category_url)
        else:
            driver.get(base_category_url.format(i))
        time.sleep(0.5)
        newlinks = get_books(driver)
        if not newlinks:
            break
        else:
            category_links += newlinks

    return category_links