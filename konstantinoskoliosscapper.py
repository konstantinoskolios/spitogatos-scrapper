from bs4 import BeautifulSoup as bs
import cfscrape
from collections import OrderedDict
import time

min_area = 40
max_rent = 500
floor = 1  # Use appropriate values (e.g., 'ypogeio', 'isogeio', 1, 2, 3)
min_bedrooms = 1

# base_url = "https://www.spitogatos.gr"
# url = f"{base_url}/enoikiaseis-katoikies/pollaples_perioxes-101,102,103,104/orofos_apo_{floor}/timi_eos-{max_rent}/emvado_apo-{min_area}/dwmatia_apo-{min_bedrooms}"

url = f"https://konstantinoskolios.tech/"

def scrape_properties(url):

    print(url)
    scraper = cfscrape.create_scraper()
    response = scraper.get(url)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None

    
    soup = bs(response.text, "html.parser")


    data = soup.find_all('div', class_='social-links')
    
    # print(data)

    # raise SystemExit

    properties = [
        {
            'class' : link.get('class'),
            'href' : link.get('href'),
            'target' : link.get('target') 
        }    

        for div in data
        for link in div.find_all('a',href=True)
    ]

    # print(properties)

    return properties

    
def save_to_file(properties,page):
    if not properties:
        print("No data to save.")
        return

    filename = f"kolios-properties-{page}.txt"
    try:
        with open(filename, "w") as file:
            for prop in properties:
                file.write(f'{prop}\n')
        print("Data saved to kolios-properties-{page}.txt")  
    except IOError as e:
        print(f"An error orccured while saving the file: {e}")

def remove_duplicates(input,output):
    
    with open(input, 'r') as file:
        lines = file.readlines()   

    unique_lines = list(OrderedDict.fromkeys(lines))

    with open(output, 'w') as file:
        file.writelines(unique_lines)

if __name__ == '__main__':
    properties = scrape_properties(f"{url}/selida_{1}")
    save_to_file(properties,1)

    # for i in range(3):
        # sleep(5)


    # remove_duplicates('properties.txt','properties_remove_duplicates.txt')        