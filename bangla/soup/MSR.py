import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('https://bangla.bdnews24.com/politics/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('li',attrs={'class':'article first '})
r2=soup.find_all('li',attrs={'class':'article '})
l=0
for r in r1+r2:
	if l<10:
	    txt=r.find('a')['href']
	    url=r.find('a').text[1:-1]
	    news.append((url,txt,'Bdnews24'))
	l+=1

"""
#--------------jugantor-----------

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


print('MSR',len(news))

for r in news:
	print(r[0])

"""