import requests
import selectorlib
from datetime import datetime

now = datetime.now()
time_string = now.strftime("%Y/%m/%d %H:%M:%S")
print(time_string)


URL = 'https://programmer100.pythonanywhere.com/'

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    content = response.text
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(content)['temperatures']
    return value

def store_data(time_string, temperature):
    with open('data.txt', 'a') as fo:
        


if __name__ == '__main__':
    # temperature = scrape(URL)
    temperature = 19
