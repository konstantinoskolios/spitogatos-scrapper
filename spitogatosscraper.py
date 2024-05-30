from bs4 import BeautifulSoup as bs
import cfscrape
from collections import OrderedDict
import time
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='output2.log',
                    filemode='w',
                    encoding='utf-8')  # Specify UTF-8 encoding
min_area = 40
max_rent = 500
floor = 1  # Use appropriate values (e.g., 'ypogeio', 'isogeio', 1, 2, 3)
min_bedrooms = 1

base_url = "https://www.spitogatos.gr"
url = f"{base_url}/enoikiaseis-katoikies/pollaples_perioxes-101,102,103,104/orofos_apo_{floor}/timi_eos-{max_rent}/emvado_apo-{min_area}/dwmatia_apo-{min_bedrooms}"

def scrape_properties(url):

    print(url)
    scraper = cfscrape.create_scraper()
    response = scraper.get(url)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None

    time.sleep(3)
    
    soup = bs(response.text, "html.parser")

    log_print(f'{soup}')
    time.sleep(3)

    data = soup.prettify()
    
    log_print(f'{data}')

    raise SystemExit

    '''
    properties = [
        {
        'class' : link.get('class')  
        }
        for din in data
        for link in div.find_all('a',href=True)
    ]
    '''


    return properties

def save_to_file(properties,page):
    if not properties:
        print("No data to save.")
        return

    filename = f"properties-{page}.txt"
    try:
        with open(filename, "w") as file:
            for prop in properties:
                file.write(f'{prop}\n')
        print("Data saved to properties-{page}.txt")  
    except IOError as e:
        print(f"An error orccured while saving the file: {e}")

def remove_duplicates(input,output):
    
    with open(input, 'r') as file:
        lines = file.readlines()   

    unique_lines = list(OrderedDict.fromkeys(lines))

    with open(output, 'w') as file:
        file.writelines(unique_lines)

def log_print(message):
    logging.info(message)

if __name__ == '__main__':
    properties = scrape_properties(f"{url}/selida_{1}")

    # for i in range(3):
        # sleep(5)
    save_to_file(properties,1)


    # remove_duplicates('properties.txt','properties_remove_duplicates.txt')        