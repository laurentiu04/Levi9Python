'''
Build a simple web scraper using beautifulsoup and requests libraries. The site you need to scrape is: https://books.toscrape.com/.
You will write a single modular script to perform three core actions:
	-Extract: Loop through the first 5 pages dynamically using requests.
	-Transform: Extract and normalize titles, convert star-ratings text ("Three") to integers (3), and strip currency symbols (Â£) from prices.
	-The output CSV should have: title,genre,rating,upc,price,availability
	-Load: Write the completely sanitized dataset into a structured CSV.
'''

from bs4 import BeautifulSoup
import requests
import pandas as pd

book_info_df = pd.DataFrame()

for page in range(1, 3):
    page_response = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html")
    soup = BeautifulSoup(page_response.text, 'html.parser')
    print(f"Scraping page {page} / 5")# check if correct page is scraped

    index = 0
    for link in soup.select('article h3 a'):
        book_link = link.get('href')
        print(f'\t#{index} | Scraping {book_link}... ', end="")
        book_page = requests.get(f"https://books.toscrape.com/catalogue/{book_link}")
        book_soup = BeautifulSoup(book_page.text, 'html.parser')

        title = book_soup.select_one('h1').text.strip()
        rating = 0
        match book_soup.select_one('.star-rating')['class'][1]:
            case 'One':
                rating = 1
            
            case 'Two':
                rating = 2

            case 'Three':
                rating = 3

            case 'Four':
                rating = 4

            case 'Five':
                rating = 5

        price = float(book_soup.select_one(".price_color").text.split("Â£")[1])
        upc = book_soup.find('td').text
        genre = book_soup.select('ul li a')[2].text
        av = book_soup.find_all('td')[5].text

        book_info = {
            "Title": [title],
            "Genre": [genre],
            "Rating": [rating],
            "UPC": [upc],
            "Price": [price],
            "Availability": [av]
        }

        book_info_df = pd.concat([book_info_df, pd.DataFrame(book_info)], ignore_index=True)
        print("Done!")
        index += 1

book_info_df.to_csv('book_scraping.csv')
