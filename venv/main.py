#importing packages to be used later
import requests
import pandas as pd
from requests_html import HTML
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
from requests_html import HTMLSession

#url = input('Please enter the URL of the site you would like to get information from: ')
#connecting to firebase

cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred)
db=firestore.client()
firebase = firebase.FirebaseApplication('https://scraping-practice-py.firebaseio.com', None)


#URL = input('Please enter the URL of the site you would like to get information from: ')


#function to get the source of a url that is passed
# def getSource(url):
#     session = HTMLSession()
#     response = session.get(url)
#     return response
# print(getSource(url))

#connects to specified url
# session=HTMLSession()
# response= session.get(url)
# returns the title of the page of the url that is passed
# title = response.html.find('title', first=True).text
# print(title)
# ref = db.reference('Database reference')

#canonical link is one used to optimize search engine searches(like a shortened version)
#canonical = response.html.xpath("//link[@rel='canonical']/@href")
# print(canonical)

#returns description of a page if one has one
# description = response.html.xpath("//meta[@name='description']/@content")


#returns author of a page
#author =  response.html.xpath("//meta[@name='author']/@content")
#print(author + description)

#gets image link from page if one has one
#image=response.html.xpath("//meta[@property='og:image']/@content")
# print(image)

def create():
    url = input('Please enter the URL of the site you would like to get information from: ')
    session = HTMLSession()
    response = session.get(url)
    title = response.html.find('title', first=True).text
    description = response.html.xpath("//meta[@name='description']/@content")
    canonical = response.html.xpath("//link[@rel='canonical']/@href")
    author = response.html.xpath("//meta[@name='author']/@content")
    image = response.html.xpath("//meta[@property='og:image']/@content")
    collectName=input("Please enter the name of the collection you would like to create. \n")
    db.collection(collectName).document(title).set(
        {'Title': title,
         'Author': author,
         'Description': description,
         'Image': image,
         'Canonical link': canonical
         }
    )

def main():
    doCrud='Y'
    while doCrud.upper()=='Y':
        crud=input("Would you like to Create,Read,Update or Delete?\n (c,r,u,d)")
        if crud.upper()=='C':
            create()
            doCrud=input('Would you like to create, read, update or delete anything else?\n(y/n): ')
main()