from datetime import datetime
import csv 
import requests 
import bs4 
import pandas as pd 


# API endpoints to mimic a real browser request
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5'
}

price_history_info = {
    'date': [],
    'open_price' : [],
    'high_price': [],
    'low_price': [],
    'close_price': []
}

def get_stock_data(soup):
    stock_date_th = soup.find('table', class_ ="table")
    print(stock_date_th.prettify())
    pass 

def get_page_html(url):
    res = requests.get(
        url=url,
        headers=REQUEST_HEADER
    )
    return res.content


def extract_stock_info(url):
    print(f"Scrapping URL {url}")
    html = get_page_html(url)

    # instantiate beautiful soup object 
    soup = bs4.BeautifulSoup(html, 'lxml')
    date = get_stock_data(soup)
    price_history_info['date'].append(date)
    




if __name__ == "__main__":
    print("Nepal Paisa Scrapping")
    
    with open('app_factory/script/srap_urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            extract_stock_info(url)

