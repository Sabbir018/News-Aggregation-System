import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('https://www.dhakatribune.com/articles/entertainment/')
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

#---------------bdnews--------------------

r=requests.get('https://bdnews24.com/entertainment/')
soup = BeautifulSoup(r.text, 'html.parser')

r1=soup.find_all('h3')

l=0
for r in r1:   #for h3 two news only
	if l<4:
	    url=r.find('a')['href']
	    txt=r.find('a').text[1:-1]
	    news.append((txt,url,"Bdnews24"))
	    
	l+=1

print("ENGLISH ENTERTAINMENT ",len(news)) 

