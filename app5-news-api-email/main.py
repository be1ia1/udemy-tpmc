import requests
import datetime

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

from send_email import send_email

url = 'https://newsapi.org/v2/everything?' \
                            'q=ubuntu&' \
                            'from=2022-12-29&' \
                            'sortBy=publishedAt&' \
                            'apiKey=0b31d5b365fb42fb8f2d249f343bf98a'

request = requests.get(url)
content = request.json()

date_now = (datetime.datetime.now()).strftime('%d-%m-%Y')

# msg = MIMEMultipart('alternative')
# msg["Subject"] = f'News about Ubuntu {date_now}'
# msg["From"] = 'News API'

message_body = ''

for article in content['articles'][:10]:
    # message_body += f"<p><b>{article['title']}</b><br>"
    # message_body += f"{article['description']}</p>"
    message_body += '{}\n'.format(article['title'])
    message_body += '{}\n'.format(article['url'])
    message_body += '{}\n\n'.format(article['description'])

message_body = message_body.encode('utf-8')

# html = f"""\
# <html>
# <body>
#     {message_body}
# </body>
# </html>
# """

# part = MIMEText(html, 'html')
# msg.attach(part)

send_email(message_body)
