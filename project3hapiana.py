import bs4
import urllib.request

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

myurl = 'https://www.otlob.com/restaurant/e6ym/desoky-soda-dokki?gclid=CjwKCAjwhLHaBRAGEiwAHCgG3omHypf_-9EPAbVwjT1nCxXkCWlz8VttIRGKIIKF57zEexsJK2cPaxoCbckQAvD_BwE'
headers={'User-Agent':user_agent,} 
request=urllib.request.Request(myurl,None,headers) #The assembled request
response = urllib.request.urlopen(request)
page_html = response.read()
page_soup = soup(page_html , 'html.parser')
containers =page_soup.findAll('div', {'class':'menu-item__content-wrapper'})
container= containers[0]
'''len(containers)'''
'''containers[0]'''

#A trial before looping 
'''item_title = container.findAll('div', {'class':'menu-item__title'})
item_name = item_title[0].text.strip()

item_price = container.findAll('div', {'class':'menu-item__variation__price'})
item_price[0].text.strip()'''

records = []
for container in containers:
    item_title = container.findAll('div', {'class':'menu-item__title'})
    item_name = item_title[0].text.strip()
    
    item_price = container.findAll('div', {'class':'menu-item__variation__price'})
    price = item_price[0].text.strip()
    records.append([item_name , price])