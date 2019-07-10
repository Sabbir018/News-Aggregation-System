import requests
from bs4 import BeautifulSoup
news=[]

#-----------for thedailystar-----------------
r=requests.get('https://www.thedailystar.net/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'highlight-text'})
r2=soup.find_all('ul',attrs={'class':'list-border'})


url='https://www.thedailystar.net'+r1[0].find('a')['href']
txt=r1[0].find('a').text
news.append((txt,url,'thedailystar'))

i=0
for r in r2:
    if i<4:
    	r=r.find('h5')
    	txt=r.find('a').text
    	url='https://www.thedailystar.net'+r.find('a')['href']
    	
    	news.append((txt, url,'thedailystar'))
    i+=1

#-----------for daily observer-----------------

r=requests.get('http://www.observerbd.com/cat.php?cd=193')
soup = BeautifulSoup(r.text, 'html.parser')
r2=soup.find_all('div',attrs={'class':"title_inner"})


for r in r2:
	url='http://www.observerbd.com/'+r.find('a')['href']
	txt=r.find('b').text
	news.append((txt,url,'Dailyobserver'))

#-------------for dhaka tribune-------------
r=requests.get('https://www.dhakatribune.com/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'report-title'})
r2=soup.find_all('div',attrs={'class':'first-right-news-style'})

url='https://www.dhakatribune.com'+r1[0].find('a')['href']
txt=r1[0].find('h1').text[1:-1]
news.append((txt,url,'Dhakatribune'))

for r in r2:
    url='https://www.dhakatribune.com'+r.find('a')['href']
    txt=r.find('h4').text[1:-1]
    news.append((txt,url,'Dhakatribune'))


print("ENGLISH BREAKING ",len(news))  


