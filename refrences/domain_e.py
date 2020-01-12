from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


url = 'https://www.key-systems.net/en/domains'
client = urlopen(url)
page = client.read()
client.close()
soup = bs(page, 'html.parser')

container = soup.findAll('div', {'class': 'zone'})
f = open('domain_scrape.txt', 'a+')
for x in container:
    f.write(x.a.text+'\n')
f.close()
