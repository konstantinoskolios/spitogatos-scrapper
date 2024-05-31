from bs4 import BeautifulSoup as bs
import cfscrape
from collections import OrderedDict
# import time
import logging
import re
import json

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     filename='test/test1.log',
#                     filemode='w',
#                     encoding='utf-8')

# Filters 
min_area = 40
max_rent = 500
floor = 1  # Use appropriate values (e.g., 'ypogeio', 'isogeio', 1, 2, 3)
min_bedrooms = 1
pageNo = 1 # How many Pages you wanna scrape, avoid too much cause you will get a ban from antibotting,  i will find a way in the future to avoid this

# Base Url
base_url = "https://www.spitogatos.gr"

# Params Url
url = f"{base_url}/enoikiaseis-katoikies/pollaples_perioxes-101,102,103,104/orofos_apo_{floor}/timi_eos-{max_rent}/emvado_apo-{min_area}/dwmatia_apo-{min_bedrooms}"


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

    # with open("holy-bible.html","r",encoding="utf-8") as file:
        # html_content = file.read()

    
    soup = bs(response.text, "html.parser")
    # soup = bs(html_content, "html.parser")


    # data = soup.prettify()
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
    sample_file_name = f"samples/sample{pageNo}.json"
    with open(sample_file_name,"w",encoding="utf-8") as outputFile:
        outputFile.write(json_string)


def log_print(message):
    logging.info(message)

if __name__ == '__main__':
    for i in range(5,7):
        properties = scrape_properties(f"{url}/selida_{i}",f"{i}")


'''
def save_to_file(properties,page):
    if not properties:
        print("No data to save.")
        return

    filename = f"properties-{page}.txt"
    try:
        with open(filename, "w") as file:
            for prop in properties:
                file.write(f'{prop}')
        print("Data saved to properties-{page}.txt")  
    except IOError as e:
        print(f"An error orccured while saving the file: {e}")    
'''