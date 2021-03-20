import tweepy
import selenium
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import re
import csv
import os
import random as rd
import numpy as np

api_key = 'E0deXoinyr7UhoCidIOTG4SaG'
api_secret_key = 'HTY7d8teT223fgSpLOtnkUJdGeWVmKIxixbQn8nap6CEz9ywJL'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKdANwEAAAAAEaa%2FvSsVwf9UkEQO0GGuqoHmdKU%3DdaKeFmI1Nv679VUmXUOC7XntENGDAAhYXVVlSBe5QitjzzQrcf'
access_token = '1243477142584737792-98oGKzRy9zyYXg9HFgLsgcHrVRzLjB'
access_token_secret = 'vGww6kYRunI0T9hK0uqZUIm4LTBTORAo1xyjBiqcGztmh'

qt_list = []

def download_quotes():
	url = "https://www.happycow.org.uk/inspiration/quotes_tolkien.xml"
	response = urlopen(Request(url))
	html = bs(response, 'html.parser')
	return html
	pass

def clean_quote(txt):
	sub_list = ['<br />','&lt;br /&gt;', '&lt;br','&lt;','/&gt;']
	for sub in sub_list:
		txt = txt.replace(sub, '')
	return txt

def list_quotes():
	html = download_quotes()
	#print(type(html))
	text = clean_quote(html.text)
	#print(text)

	qt_list = re.split(r"\n\n", text)
	i=0

	a  = rd.randint(5, 359)
	#print(len(qt_list))
	print(qt_list[a]) 

	for qt in qt_list:
		#print("Quote : ", i, qt)
		i+=1



auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


list_quotes()

api = tweepy.API(auth)
#print(api.me())

	