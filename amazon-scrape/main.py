import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP
from datetime import datetime
import re

TO_EMAIL = "jijo4565-jdhiujhu345@yahoo.co.jp"
FROM_EMAIL = "dkgi345sd90@gmail.com"
FROM_PASSWORD = "dij345iois"
AMAZON_URL = "https://www.amazon.co.jp/%E3%82%B3%E3%82%B9%E3%82%AE%E3%82%BC%E3%83%B3-Kosugizen-%E5%BE%B3%E7%94%A8%E3%82%AB%E3%83%A9%E3%83%BC%E3%82%BF%E3%82%AA%E3%83%AB10%E8%89%B2%E7%B5%84/dp/B01M08KCYI/ref=sr_1_7?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E3%82%BF%E3%82%AA%E3%83%AB&qid=1613723978&sr=8-7"

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
currency =  f"{year}年{month}月{day}日"
# print(currency)

response = requests.get(AMAZON_URL, headers={"User-Agent":"Defined"}).text
# print(response)

soup = BeautifulSoup(response, "lxml")
price_source = soup.find(name="span", id="priceblock_ourprice", class_="priceBlockBuyingPriceString").getText()
price = re.sub(r'[￥,]', "", price_source)
item_name = soup.find(name="h1", id="title").text.strip()




if int(price) < 10000:
    message = f"The price of {item_name} dropped to {currency}{price}\nHere's the link: {AMAZON_URL}"

    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=FROM_PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert \n\n{message}".encode("utf8")
        )

