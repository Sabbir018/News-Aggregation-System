import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('http://www.observerbd.com/cat.php?cd=187')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'title_inner'})

l=0
for r in r1:   #for h3 two news only
	if l<6:
	    url='http://www.observerbd.com/'+r.find('a')['href']
	    t=r.find('a')
	    txt=r.find('b').text
	    news.append((txt,url,"observer"))
	   
	l+=1
#---------------for daily star--------------
r=requests.get('https://www.thedailystar.net/world')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':"highlight-text"})
r2=soup.find_all('ul',attrs={'class':"list-border list-border-dotted margin-bottom-big"})


url='https://www.thedailystar.net'+r1[0].find('a')['href']
txt=r1[0].find('a').text
news.append((txt,url,"Dailystar"))

url='https://www.thedailystar.net'+r2[0].find('a')['href']
txt=r2[0].find('a').text
news.append((txt,url,"Dailystar"))
#-----------------------for dhakatribune------------

r=requests.get('https://www.dhakatribune.com/articles/world/')
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

print('English International',len(news))
