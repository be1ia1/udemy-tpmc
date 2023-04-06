import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

# "INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
# SELECT * FROM events WHERE date="2088.10.15"

URL = 'https://programmer100.pythonanywhere.com/tours/'


class Email:
    def send(self, message):
        host = 'smtp.gmail.com'
        port = 465
        username = 'belial.agula@gmail.com'
        password = os.getenv('email_password')
        receiver = 'gula@pr.km.ua'

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url)
        content = response.text
        extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
        value = extractor.extract(content)['tours']
        return value


class Database:

    def __init__(self,database_path) -> None:
        self.connection = sqlite3.connect(database_path)

    def get_event(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events")
        events = cursor.fetchall()
        return events

    def store_event(self, extracted):
        cursor = self.connection.cursor()
        cursor.executemany("INSERT INTO events VALUES (?,?,?)", extracted)
        self.connection.commit()
    

if __name__ == '__main__':

    count = 1
    while count <= 10:
        print(f'Start {count} step..')
        event = Event()
        extracted = event.scrape(URL)
        if extracted != 'No upcoming tours':
            extracted = tuple(i.strip() for i in extracted.split(','))
            database = Database(database_path='data.db')
            if not extracted in database.get_event():
                print(f'Add {extracted} in database..')
                database.store_event([extracted])
                email = Email()
                # email.send()
            else:
                print(f'{extracted} already presented in database..')
        count += 1
        time.sleep(5)