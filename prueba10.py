from urllib.request import urlopen
 
from bs4 import BeautifulSoup
import requests
import urllib
import sys

def run(adults):
	html = urlopen("https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAEoggJCAlhYSDNYBGjtAYgBAZgBCsIBCndpbmRvd3MgMTDIAQzYAQPoAQGSAgF5qAID&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.es.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNYBGjtAYgBAZgBCsIBCndpbmRvd3MgMTDIAQzYAQPoAQGSAgF5qAID%3Bcheckin_month%3D1%3Bcheckin_monthday%3D1%3Bcheckin_year%3D2019%3Bcheckout_month%3D1%3Bcheckout_monthday%3D9%3Bcheckout_year%3D2019%3Bcity%3D-907232%3Bclass_interval%3D1%3Bdest_id%3D-907232%3Bdest_type%3Dcity%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D45%3Braw_dest_type%3Dcity%3Broom1%3DA%252CA%3Brows%3D45%3Bsb_price_type%3Dtotal%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bss%3DLa%2520Paloma%3Bssb%3Dempty%3Bssne%3DLa%2520Paloma%3Bssne_untouched%3DLa%2520Paloma%26%3B&ss=La+Paloma&ssne=La+Paloma&ssne_untouched=La+Paloma&city=-907232&checkin_year=2019&checkin_month=1&checkin_monthday=1&checkout_year=2019&checkout_month=1&checkout_monthday=9&group_adults=" + adults +"&group_children=0&no_rooms=1&from_sf=1")
	 
	res = BeautifulSoup(html.read(),"html5lib");
	
	filename = 'page.html'
	f = open(filename,'wb')
	f.write("<!DOCTYPE html><html>".encode('utf-8'))

	links = res.find_all('link')
	scripts = res.find_all('script')

	for link in links:
		f.write(link.encode('utf-8'))
	for script in scripts:
		f.write(script.encode('utf-8'))

	f.write("<body>".encode('utf-8'))
	#print(page)
	parentDiv = res.find('div', {"id": 'hotellist_inner'})
	cards = parentDiv.find_all('div')
	for card in cards:
		f.write(card.encode('utf-8'))
		try:
			textContent = card.find_all('div')[1]
			print(textContent)
		except Exception as e:
			print('Exception in textContent')
		try:
			childTextContent = textContent.find('div',{"class":{'sr_item_content', 'sr_item_content_slider_wrapper'}})
		except Exception as e:
			print('exception in childtexcontet')
		try:		
			roomDetails = childTextContent.find('div', {"class":'room_details'})
		except Exception as e:
			print('exception in roomDetails')
		try:	
			importantText = roomDetails.find('div', {"class": 'sr-group_recommendation'})
		except Exception as e:
			print('Exception in importantText')
		try:	
			price = importantText.find_all('div')[0]
			print(price)
		except:
			print('Exception in price')	
	f.write("<p>Estoy funcionando para el carajo</p>".encode('utf-8'))
	f.write("</body></html>".encode('utf-8'))
	#f.write(res.encode('utf-8'))
	f.close()

if __name__ == '__main__':
	if len(sys.argv) == 2:
		run(sys.argv[1])
	else:
		print ("Error: enter one url")