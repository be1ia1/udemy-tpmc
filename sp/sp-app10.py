import requests
import selectorlib
from datetime import datetime
import time
import sqlite3


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
        fo.write(f"{time_string},{temperature}")

def store_data_sql(connection, item):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO items VALUES (?,?)", item)
    connection.commit()

if __name__ == '__main__':
    connection = sqlite3.connect('data.db')
    count = 1
    while count <= 10:
        print(f'Start {count} step..')
        count += 1
        now = datetime.now()
        time_string = now.strftime("%Y/%m/%d %H:%M:%S")
        temperature = scrape(URL)
        item = [(time_string, int(temperature))]
        # store_data(time_string, temperature + '\n')
        store_data_sql(connection, item)
        time.sleep(15)