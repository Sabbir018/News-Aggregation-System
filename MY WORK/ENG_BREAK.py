import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('https://bdnews24.com/')
soup = BeautifulSoup(r.text, 'html.parser')
#r1=soup.find_all('div',attrs={'class':'text'})
r1=soup.find_all('h1',attrs={'class':'default'})
r2=soup.find_all('h6',attrs={'class':'default'})
r3=soup.find_all('h3',)

url=r1[0].find('a')['href']
txt=r1[0].find('a').text[0:-1]
news.append((txt,url,'Bdnews24'))

l=0
for r in r3:   #for h3 two news only
	if l<2:
	    txt=r.find('a')['href']
	    url=r.find('a').text[1:-1]
	    news.append((url,txt,"Bdnews24"))
	l+=1

l=0
for r in r2:           #for h6 we take first 4 news only
	if l<4:
	    txt=r.find('a')['href']
	    url=r.find('a').text[1:-1]
	    news.append((url,txt,"Bdnews24"))
	l+=1


print("BDNEWS BREAKING ",len(news))  
