# Book Scraper

This project is a web scraper for the [Books to Scrape](https://books.toscrape.com) website. It uses Selenium to navigate through the website and BeautifulSoup to parse the HTML content. The scraper collects information about books from different categories and saves the data into a CSV file.

## Features

- Scrapes book information from the Travel and Nonfiction categories.
- Collects details such as title, price, star rating, product description, and more.
- Saves the collected data into a CSV file.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- pandas
- requests

## Installation

1. Clone the repository:

    ```sh
    git clone (https://github.com/ahmettsadik/WebScrapping_BookInfos)
    cd WebScrapping_BookInfos
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:

    ```sh
    python main.py
    ```

2. The script will navigate through the Travel and Nonfiction categories on the Books to Scrape website, collect book information, and save it into a CSV file named `Books.csv`.

## Project Structure

- `main.py`: The main script that initializes the web driver, navigates through the categories, and collects book information.
- `utils.py`: Contains utility functions such as `get_books`, `get_books_info`, and `get_category_links`.
- `requirements.txt`: Lists the required Python packages.

## Functions

### `get_books(driver)`

Fetches the book links from the current page.

**Parameters:**
- `driver`: The Selenium WebDriver instance.

**Returns:**
- A list of book links.

### `fetch_book_info(book_url)`

Fetches the book information from the given URL.

**Parameters:**
- `book_url`: The URL of the book.

**Returns:**
- A dictionary containing the book information.

### `get_books_info(links)`

Fetches the book information for a list of book links.

**Parameters:**
- `links`: A list of book links.

**Returns:**
- A pandas DataFrame containing the book information.

### `get_category_links(driver, category_element)`

Fetches the book links from all pages of a given category.

**Parameters:**
- `driver`: The Selenium WebDriver instance.
- `category_element`: The Selenium WebElement representing the category.

**Returns:**
- A list of book links.

