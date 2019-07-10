import requests

from bs4 import BeautifulSoup
news=[]

r=requests.get('https://bdnews24.com/cricket/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('h3')
r2=soup.find_all('h2')

txt=r1[0].find('a')['href']
url=r1[0].find('a').text[1:-1]
news.append((url,txt,"Bdnews24"))

l=0
for r in r2:   #for h3 two news only
	if l<5:
	    txt=r.find('a')['href']
	    url=r.find('a').text[1:-1]
	    news.append((url,txt,"Bdnews24"))
	l+=1

print("BDNEWS BREAKING ",len(news))  
for r in news:
	print(r[0])