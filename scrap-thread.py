import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import threading

start = time.time()


def process1():
    url = "https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA~Category~39~page~2"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select('.maintitle')
    price = soup.select('.prd-price span')

    list_title = [t.text for t in title]
    list_price = [int(p.text.replace(',', '')) for p in price]

    database = dict(list(zip(list_title, list_price)))

    df = pd.DataFrame(list(database.items()), columns=['قیمت', 'گوشی'])
    df = df.dropna()
    print(df)

    high_price_phone = df.loc[df['گوشی'].idxmax()]
    low_price_phone = df.loc[df['گوشی'].idxmin()]

    print("\nگران‌ترین گوشی: ", high_price_phone['گوشی'])
    print("ارزان‌ترین گوشی: ", low_price_phone['گوشی'])

def process2():
    url = "https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA~Category~39~page~3"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select('.maintitle')
    price = soup.select('.prd-price span')

    list_title = [t.text for t in title]
    list_price = [int(p.text.replace(',', '')) for p in price]

    database = dict(list(zip(list_title, list_price)))

    df = pd.DataFrame(list(database.items()), columns=['قیمت', 'گوشی'])
    df = df.dropna()
    print(df)

    high_price_phone = df.loc[df['گوشی'].idxmax()]
    low_price_phone = df.loc[df['گوشی'].idxmin()]

    print("\nگران‌ترین گوشی: ", high_price_phone['گوشی'])
    print("ارزان‌ترین گوشی: ", low_price_phone['گوشی'])


t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(end - start)
