import requests
import selectorlib
import smtplib, ssl
import os


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

def store_event(extracted):
    with open('events.txt', 'a') as fo:
        fo.write(extracted + '\n')

def get_event():
    with open('events.txt') as fo:
        events = fo.read()
    return events

if __name__ == '__main__':
    extracted = scrape(URL)
    print(extracted)
    if extracted != 'No upcoming tours':
        if not extracted in get_event():
            store_event(extracted)
            send_email(message='Hey, new event was found!')
