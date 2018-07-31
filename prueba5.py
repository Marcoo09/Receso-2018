from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup
 
html = urlopen("https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAEoggJCAlhYSDNYBGjtAYgBAZgBCsIBCndpbmRvd3MgMTDIAQzYAQPoAQGSAgF5qAID;sid=b85ecdd092a9d8298b05fd8be063d977;checkin_monthday=1&checkin_year_month=2019-1&checkout_monthday=9&checkout_year_month=2019-1&class_interval=1&dest_id=-907232&dest_type=city&do_availability_check=1&dtdisc=0&group_adults=2&group_children=0&highlighted_hotels=1414122&hp_avform=1&inac=0&index_postcard=0&label_click=undef&no_rooms=1&offset=0&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&src=hotel&ss_all=0&ssb=empty&sshis=0&#sort_by")
 
res = BeautifulSoup(html.read(),"html5lib");


titles = res.findAll('span', { "class": "sr-hotel__name"})
qualifies = res.findAll("span",{"class": "review-score-badge"})

for title in titles:
	print(title.getText())


for qualify in qualifies:
	print(qualify.getText())	
