import requests
from datetime import datetime, timedelta

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from send_email import send_email

topic = 'ubuntu'

date_now = datetime.now()
query_date = (date_now + timedelta(days=-31)).strftime('%Y-%m-%d')

url = 'https://newsapi.org/v2/everything?' \
                            f'q={topic}&' \
                            'language=en&' \
                            f'from={query_date}&' \
                            'sortBy=publishedAt&' \
                            'apiKey=0b31d5b365fb42fb8f2d249f343bf98a'

response = requests.get(url)
content = response.json()

date_now = date_now.strftime('%d-%m-%Y')

msg = MIMEMultipart('alternative')
msg["Subject"] = f'News about Ubuntu {date_now}'
msg["From"] = 'News API'

message_body = ''

for article in content['articles'][:10]:
    message_body += f"<p><a href={article['url']}><b>{article['title']}</b></a><br>"
    message_body += f"{article['description']}</p>"

html = f"""\
<html>
<body>
    {message_body}
</body>
</html>
"""

part = MIMEText(html, 'html')
msg.attach(part)
send_email(msg.as_string())
