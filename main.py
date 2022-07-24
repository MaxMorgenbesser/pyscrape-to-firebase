import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
url = input('Please enter the URL of the site you would like to get information from: ')
# def getSource(url):
#     session = HTMLSession()
#     response = session.get(url)
#     return response
# print(getSource(url))
session=HTMLSession()
response= session.get(url)
title = response.html.find('title', first=True).text
print(title)
canonical = response.html.xpath("//link[@rel='canonical']/@href")
print(canonical)
description =  response.html.xpath("//meta[@name='description']/@content")
author =  response.html.xpath("//meta[@name='author']/@content")
print(author,description)

