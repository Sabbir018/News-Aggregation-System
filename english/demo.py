import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('https://www.jugantor.com/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'id':'popular_list_block'})
url=r1[0].find('a')
r=r1[0].find('a')
txt=r.find('h4').text
news.append((txt,url,"Jugantor"))


r1=soup.find_all('div',attrs={'class':'editor_picks_list'})

l=0
for r in r1:
	if l<6:
		url=r.find('a')['href']
		txt=r.find('a')
		txt=txt.find('h4').text
		news.append((txt,url,"Jugantor"))
	l+=1



