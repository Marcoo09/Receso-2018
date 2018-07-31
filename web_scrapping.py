import urllib.request
import requests
from bs4 import BeautifulSoup
import urllib



def run():
	for i in range(1,11):
		response = requests.get('https://www.booking.com/searchresults.es.html?aid=376374&label=esrow-OtlvhU2CXhSVxek50Z_17wS267754636757%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap1t1%3Aneg%3Afi%3Atikwd-65526620%3Alp1012872%3Ali%3Adec%3Adm&sid=b85ecdd092a9d8298b05fd8be063d977&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Faid%3D376374%3Blabel%3Desrow-OtlvhU2CXhSVxek50Z_17wS267754636757%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap1t1%253Aneg%253Afi%253Atikwd-65526620%253Alp1012872%253Ali%253Adec%253Adm%3Bsid%3Db85ecdd092a9d8298b05fd8be063d977%3Bsb_price_type%3Dtotal%26%3B&ss=La+Paloma&checkin_year=&checkin_month=&checkout_year=&checkout_month=&no_rooms=1&group_adults=8&group_children=0&b_h4u_keep_filters=&from_sf=1&ss_raw=La+p&dest_id=&dest_type=&search_pageview_id=bc8105e30c2f0042&search_selected=false')
		soup = BeautifulSoup(response.content, 'html.parser')
		image_container = soup.find(id = 'logo_no_globe_new_logo')

		image_url = image_container.find('img')['src']
		image_name = image_url.split('/')[-1]
		print('Descargando la imagen {}'.format(image_name))
		urllib.request.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == '__main__':
	run()