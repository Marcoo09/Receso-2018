""" Download images of a website
Doing by Marco Fiorito - 24/07/18
"""
from urllib.request import urlopen
 
from bs4 import BeautifulSoup
import requests
import urllib
from urllib.error import URLError

html = urlopen("https://www.booking.com/index.es.html?label=gen173nr-1DCAEoggJCAlhYSDNYBGjtAYgBAZgBCsIBCndpbmRvd3MgMTDIAQzYAQPoAQGSAgF5qAID;sid=b85ecdd092a9d8298b05fd8be063d977;sb_price_type=total&")
 
res = BeautifulSoup(html.read(),"html5lib");
 
print(res.title)
"""print(res.find_all('img'))"""
a = res.find_all('img')
for i in a:
	"""print(i['src']) """
	try: 
		image_url = i['src']
		image_name = image_url.split('/')[-1]
		print('Descargando la imagen {}'.format(image_name))
	except Exception as e:
		print("Error al obtener el src")
	try:
		urllib.request.urlretrieve(image_url, image_name)
	except Exception as e:
		print( "Error {}".format(e))
