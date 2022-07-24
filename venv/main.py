#importing packages to be used later
import requests
import pandas as pd
from requests_html import HTML
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from requests_html import HTMLSession

URL = input('Please enter the URL of the site you would like to get information from: ')
#connecting to firebase

cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': "URL to database"
})


#gets the url that can be used to find data from

#URL = input('Please enter the URL of the site you would like to get information from: ')


#function to get the source of a url that is passed
# def getSource(url):
#     session = HTMLSession()
#     response = session.get(url)
#     return response
# print(getSource(url))

#connects to specified url
session=HTMLSession()
response= session.get(url)
# returns the title of the page of the url that is passed
title = response.html.find('title', first=True).text
print(title)
ref = db.reference('Database reference')

#canonical link is one used to optimize search engine searches(like a shortened version)
canonical = response.html.xpath("//link[@rel='canonical']/@href")
print(canonical)

#returns description of a page if one has one
description = response.html.xpath("//meta[@name='description']/@content")


#returns author of a page
author =  response.html.xpath("//meta[@name='author']/@content")
print(author + description)

#gets image link from page if one has one
image=response.html.xpath("//meta[@property='og:image']/@content")
print(image)
