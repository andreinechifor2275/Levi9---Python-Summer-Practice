# 1. Write a Python script that fetches the HTML content of https://webscraper.io/test-sites/e-commerce/static
# and prints all the hyperlinks (href attributes of <a> tags) found on the page
import requests
from bs4 import BeautifulSoup
#
#
# url = 'https://webscraper.io/test-sites/e-commerce/static'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title.text)
#
# links = soup.find_all('a')
#
# for link in links:
#     href = link.get('href')
#     if href is not None:
#         print(href)


# # 2. Write a Python script that fetches the HTML content of https://webscraper.io/test-sites/e-commerce/static
# # and prints all prices
#
#
# url = 'https://webscraper.io/test-sites/e-commerce/static'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# print("Page Title:", soup.title.text)
#
#
# prices = soup.find_all('span', class_='price')
#
# print("Prices found:")
# for price in prices:
#     print(price.text)

# 3. Write a Python script that downloads all images (src attributes of <img> tags) from https://example.com
# and saves them locally

# import requests
# from bs4 import BeautifulSoup
# import os
# from urllib.parse import urljoin
#
# url = 'https://example.com'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
#
# os.makedirs('downloaded_images', exist_ok=True)
#
#
# img_tags = soup.find_all('img')
#
# print(f"Found {len(img_tags)} images.")
#
# for img in img_tags:
#     img_url = img.get('src')
#     if img_url:
#
#         img_url = urljoin(url, img_url)
#         try:
#
#             img_data = requests.get(img_url).content
#
#             img_name = img_url.split('/')[-1]
#
#             with open(f'downloaded_images/{img_name}', 'wb') as f:
#                 f.write(img_data)
#             print(f"Downloaded {img_name}")
#         except Exception as e:
#             print(f"Failed to download {img_url}: {e}")

#4. Write a Python script that scrapes all rows from the table on https://www.w3schools.com/html/html_tables.asp
# and saves the data into a CSV file

# import requests
# from bs4 import BeautifulSoup
# import csv
#
# url = 'https://www.w3schools.com/html/html_tables.asp'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
#
# table = soup.find('table', id='customers')
#
#
# headers = []
# for th in table.find_all('th'):
#     headers.append(th.text.strip())
#
#
# rows = []
# for tr in table.find_all('tr')[1:]:
#     cells = tr.find_all('td')
#     if cells:
#         row = [cell.text.strip() for cell in cells]
#         rows.append(row)
#
#
# with open('w3schools_table.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(rows)
#
# print("Table data has been saved to 'w3schools_table.csv'")

# 5. Write a Python script that scrapes product names from the first 3 pages of
# https://webscraper.io/test-sites/e-commerce/static/computers/laptops and prints them

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


product_tags = soup.find_all('a', class_='title')


products_per_page = 10
total_pages = 3
total_products = products_per_page * total_pages

print(f"Product names from first {total_pages} pages:\n")

for i, product in enumerate(product_tags[:total_products], start=1):
    print(f"{i}. {product.text.strip()}")







