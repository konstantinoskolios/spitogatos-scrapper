from bs4 import BeautifulSoup as bs
import cfscrape
from collections import OrderedDict
import logging
import re
import json
import argparse

# Base Url
base_url = "https://www.spitogatos.gr"

# Regex Patterns
location_pattern = re.compile(r'\((.*?)\)')
title_pattern = re.compile(r'\d+τ\.μ\.')
price_pattern = re.compile(r'\d+')

def scrape_properties(url,pageNo):

    print(url)
    scraper = cfscrape.create_scraper()
    response = scraper.get(url)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None

    soup = bs(response.text, "html.parser")

    data = soup.findAll('article',class_='ordered-element')    

    properties = {}

    for d in data:
        title = d.find('h3',class_='tile__title').text.strip()
        location = d.find('h3',class_='tile__location').text.strip()
        price = d.find('p',class_='price__text').text.strip()
        href = d.find('a',class_='tile__link')["href"]

        ''' 
        Apply the Regexs
        '''
        href_apply_pref = f"{base_url}{href}"
        location_apply_pattern = re.search(location_pattern, location).group(1)
        title_apply_pattern = re.search(title_pattern, title).group()
        price_apply_pattern = re.search(price_pattern,price).group()

        result = {
            "price" : price_apply_pattern,
            "title" : title_apply_pattern,
            "location" : location_apply_pattern,
        }

        properties[href_apply_pref] = result

    json_string = json.dumps(properties, indent=4, ensure_ascii=False)
    sample_file_name = f"samples/{url_to_filename(url)}"
    with open(sample_file_name,"w",encoding="utf-8") as outputFile:
        outputFile.write(json_string)

def log_print(message):
    logging.info(message)
    
import os

def url_to_filename(url):
    url = url.replace('https://www.spitogatos.gr/', '')
    url = re.sub(r'[^a-zA-Z0-9-_./]+', '_', url)
    url = url.strip('_')
    url = re.sub(r'_{2,}', '_', url)
    url = url.replace('/', '-')
    url += '.json'
    return url


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape properties from multiple pages.')
    parser.add_argument('url', type=str, help='Base URL for scraping')
    parser.add_argument('start_page', type=int, help='Start page number')
    parser.add_argument('end_page', type=int, help='End page number')
    args = parser.parse_args()

    for i in range(args.start_page, args.end_page + 1):
        properties = scrape_properties(f"{args.url}/selida_{i}", f"{i}")