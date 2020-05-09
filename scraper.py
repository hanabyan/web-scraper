import requests
from bs4 import BeautifulSoup
import re

def get_midtrans_payment_method():
    response = requests.get('https://api-docs.midtrans.com/')
    soup = BeautifulSoup(response.text, "html.parser")
    el = soup.find_all("pre", attrs={"class":"highlight JSON"})
    el_contains_payment_type = []
    for e in el:
        if e.find(text=re.compile("payment_type")):
            el_contains_payment_type.append(e)
    return el_contains_payment_type