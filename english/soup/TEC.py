import requests

from bs4 import BeautifulSoup
news=[]

#------------------Dailystar---------------
r=requests.get('https://www.thedailystar.net/science')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'list-content'})
l=0
for r in r1:
	if l<5:
		url='https://www.thedailystar.net'+r.find('a')['href']
		txt=r.find('a').text
		news.append((txt,url,"Dailystar"))
	l+=1

#----------------dhaka tribune------------
r=requests.get('https://www.dhakatribune.com/articles/science/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'top-news-cont list-para'})
r2=soup.find_all('h4',attrs={'class':'news-title'})

t=[]
u=[]
l=0
for r in r1:
	if l<10:
		url='https://www.dhakatribune.com'+r.find('a')['href']
		u.append(url)

l=0
for r in r2:
	if l<10:
		txt=r.text[1:-1]
		t.append(txt)

for i in range(10):
	news.append((t[i],u[i],'dhakatribune'))

print('ENG Tecnology',len(news))