import smtplib
from email.message import EmailMessage
import imghdr

SENDER = 'belial.ahula@gmail.com'
PASSWORD = 'tumssajhetkvtsjw'

def send_email(image):
    print('start mail process')
    email_message = EmailMessage()
    email_message['Subject'] = 'New customer showed up!'
    email_message.set_content('Hey, we just saw a new customer!')
    with open(image, 'rb') as fo:
        content = fo.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, SENDER, email_message.as_string())
    gmail.quit()
    print('end mail process')

if __name__ == '__main__':
    send_email('images/7.png')