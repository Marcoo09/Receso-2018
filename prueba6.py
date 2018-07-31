from urllib.request import urlopen
 
from bs4 import BeautifulSoup
import requests
import urllib
import sys

def run(url):
	html = urlopen(url)
	 
	res = BeautifulSoup(html.read(),"html5lib");

	page = res.find_all()
	print(page)
	filename = 'page.html'
	f = open(filename,'wb')

	f.write(res.encode('utf-8'))
	f.close()

if __name__ == '__main__':
	if len(sys.argv) == 2:
		run(sys.argv[1])
	else:
		print ("Error: enter one url")
