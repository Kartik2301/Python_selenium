from lib2to3.pgen2 import driver
from os import link
from django.http import response
from matplotlib.pyplot import title
from selenium import webdriver
from bs4 import BeautifulSoup
from constants import chrome_driver_path, google_forms_path
import time
import requests

def get_property_data():
    # response = requests.get("https://www.zillow.com/homes/New-York,-NY_rb/")
    # response.raise_for_status()

    # data = response.text

    # soup = BeautifulSoup(data, "html.parser")

    # with open("data-filling/cache.html", mode="w") as file:
    #     file.write(soup.prettify())

    # print(soup.prettify())

    with open("data-filling/cache.html", mode="r", encoding="utf8") as file:
        data = file.read()

    soup = BeautifulSoup(data, "html.parser")

    links = soup.select(selector="div#grid-search-results ul li article div.list-card-top a")
    prices = soup.select(selector="div#grid-search-results ul.photo-cards li article div.list-card-info div.list-card-heading div.list-card-price")
    addresses = soup.select(selector="div#grid-search-results ul.photo-cards li article div.list-card-info a address")

    for i in range(len(links)):
        links[i] = links[i]['href']

    for i in range(len(prices)):
        prices[i] = prices[i].getText()

    for i in range(len(addresses)):
        addresses[i] = addresses[i].getText().strip()
    
    properties = []

    for i in range(len(links)):
        properties.append({
            'link' : links[i],
            'price' : prices[i],
            'address' : addresses[i]
        })

    return properties

def add_to_form():
    data = get_property_data()
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(google_forms_path)
    time.sleep(3)

    for prop in data:     
        addr = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        addr.send_keys(prop['address'])
        price.send_keys(prop['price'])
        link.send_keys(prop['link'])
        submit.click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
        time.sleep(5)


add_to_form()
