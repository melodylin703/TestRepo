from bs4 import BeautifulSoup
import requests
import spacy
#nlp = spacy.load("en_core_web_sm")
URL = requests.get("https://www.livenation.com.tw/")
soup = BeautifulSoup(URL.text, "html.parser")
events = soup.find_all("li")
for event in events:
    print(event.text)

print("---------------------------------------------------------------------------------------------")

detail = requests.get("https://www.livenation.com.tw/event/2025-bibi-1st-world-tour-eve-in-taipei-taipei-tickets-edp1602074")
soup2 = BeautifulSoup(detail.text, "html.parser")
info = soup2.find_all("p")
for info in info:
    print(info.text)