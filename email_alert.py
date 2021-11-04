import requests
import smtplib
from bs4 import BeautifulSoup


def get_price():
    html = requests.get(f"https://www.amazon.co.uk/Yamaha-PSR-E463-Portable-Keyboard/dp/B07C34BRVG/ref=sr_1_36?crid=CGIOZJGEZ1FN&keywords=yamaha+touch+sensitive+keyboard&qid=1635986860&sprefix=yamaha+touch%2Caps%2C81&sr=8-36").json()
    soup = BeautifulSoup(html, 'html.parser')
    price = [i.get_text() for i in soup.find_all()]
    low_price = ''.join(price)[2:8]
    low_price = int(low_price.replace(',', ''))
    
    if low_price < 260:
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mypersonal@gmail.com', password)
    subject = "Now Price dropped"
    body = "check this link : https://www.amazon.in/Apple-iPhone-11-64GB-Green/dp/B07XVKBY68/ref=sr_1_7?keywords=iphone+11&qid=1573668357&sr=8-7"
    message = f"Subject:{subject}{body}"
    server.sendmail('mypersonal@gmail.com', 'mypersonal@gmail.com', message)
    print ("Successfully email alert sent")
    server.quit()