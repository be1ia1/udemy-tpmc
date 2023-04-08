import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

# "INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
# SELECT * FROM events WHERE date="2088.10.15"

URL = 'https://programmer100.pythonanywhere.com/tours/'

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'belial.agula@gmail.com'
    password = os.getenv('email_password')
    receiver = 'gula@pr.km.ua'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    content = response.text
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(content)['tours']
    return value

def get_event_sql(cursor):
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    return events

def store_event_sql(cursor, extracted):
    events = cursor.executemany("INSERT INTO events VALUES (?,?,?)", extracted)
    connection.commit()
    

def store_event(extracted):
    with open('events.txt', 'a') as fo:
        fo.write(extracted + '\n')

def get_event():
    with open('events.txt') as fo:
        events = fo.read()
    return events

if __name__ == '__main__':
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    count = 1
    while count <= 10:
        print(f'Start {count} step..')
        extracted = scrape(URL)
        if extracted != 'No upcoming tours':
            extracted = tuple(i.strip() for i in extracted.split(','))
            if not extracted in get_event_sql(cursor):
                print(f'Add {extracted} in database..')
                store_event_sql(cursor, [extracted])
                # send_email(message='Hey, new event was found!')
            else:
                print(f'{extracted} already presented in database..')
        count += 1
        time.sleep(5)