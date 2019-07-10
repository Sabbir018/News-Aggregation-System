import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('https://www.bbc.com/bengali')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':"dove-item__body"})
r2=soup.find_all('div',attrs={'class':"buzzard-item"})

url='https://www.bbc.com'+r2[0].find('a')['href']
t=r2[0].find('a')
txt=t.find('h3').text[1:-1]
author="BBC-bangla"
news.append((txt,url,author))

l=0
for r in r1:
	if l<=3:
		
		t=r.find('a')
		
		txt=t.find('h3').text[1:-1]
		url='https://www.bbc.com'+r.find('a')['href']
		author='BBC-bangla'
		news.append((txt,url,author))

	l+=1
#-----------------prothom alo----------
r=requests.get('http://www.prothomalo.com/')
soup = BeautifulSoup(r.text, 'html.parser')

r1=soup.find_all('div',attrs={'class':'col col1'})


l=0
for r in r1:
    if l<12:
        url='http://www.prothomalo.com/'+r.find('a')['href']
        t=r.find('h2')
        txt=t.find('span').text
        news.append((txt,url,'prothom alo'))
    l+=1



# for daily star


r=requests.get('https://www.thedailystar.net/bangla/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'highlight-text'})
r2=soup.find_all('div',attrs={'class':'two-50'})

url='https://www.thedailystar.net'+r1[0].find('a')['href']
txt=r1[0].find('a').text
news.append((txt,url,'dailystar'))

i=0
for r in r2:
    if i<2:
        rm=r.find('h3')
        txt=rm.find('a').text
        url='https://www.thedailystar.net'+rm.find('a')['href']
        author='dailystar'
        news.append((txt, url,author))

    i+=1

r=requests.get('https://bangla.bdnews24.com/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('h1',attrs={'class':'default'})
r2=soup.find_all('h6',attrs={'class':'default'})



url=r1[0].find('a')['href']
txt=r1[0].find('a').text[1:-1]
news.append((txt,url,'Bdnews24'))


for r in r2:
    txt=r.find('a')['href']
    url=r.find('a').text[1:-1]
    news.append((url,txt,"Bdnews24"))
   



print('breaking news',len(news))