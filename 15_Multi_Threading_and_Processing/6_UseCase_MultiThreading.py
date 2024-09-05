"""
Real World example: MultiThreading for I/O bound tasks
Scenario : Web Scraping
Web scraping often involves making numerous network requests to fetch web pages. These tasks are I/O bound because they spend
a lot of time waiting for responses from the servers. Multithreading can significantly improve the performance by allowing multiple 
web pages to be fetched concurrently.

"""

import threading
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import httpx
from selectolax.parser import HTMLParser
import time

urls = ["https://www.rei.com/c/footwear/f/scd-deals",
"https://www.rei.com/c/camping-and-hiking/f/scd-deals",
"https://www.rei.com/c/cycling/f/scd-deals",
"https://www.rei.com/c/fitness/f/scd-deals"]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"}
def fetch_content(url):
    response = httpx.get(url, headers=headers)
    html_parser = HTMLParser(response.text) # html parser
    print(f'Fetched {len(html_parser.text())} characters from {url}')
start = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
end = time.time()
print(f"Finished in : {end - start} seconds")
print("All webpages fetched")

