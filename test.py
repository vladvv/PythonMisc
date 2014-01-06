#!/usr/bin/python

# import modules
import sys, urllib.request, re
from random import choice

PAGE_URL = "http://www.reddit.com/r/wallpapers"


def pullPageText(address):
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Fakebrowser/4.2' )]

	try:
		web_handle = opener.open(address)
	except Exception as e:
		print("URL Error", e)
		sys.exit(1)
		
	return web_handle.read()

def extractImages(text):
	#images = re.findall( b'<a .*href=("http://i.imgur[^"]*)' , text )
	images = re.findall( b'href="(http://i\.imgur\.com/[^"]*)"' , text )
	return images
	
	
def printList(list):
	for item in list:
		print(item)
		print('\n')
	
	
#code starts here
page_text = pullPageText(PAGE_URL)
image_list = extractImages(page_text)



printList(image_list)
print("Length of list: ", len(image_list) )
print( choice(image_list ) )