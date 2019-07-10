import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('http://www.prothomalo.com/bangladesh-politics')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'col col1'})
l=0
for r in r1:
	
		url='http://www.prothomalo.com/'+r.find('a')['href']
		t=r.find('h2')
		txt=t.find('span').text
		news.append((txt,url,'prothom alo'))



r=requests.get('https://bangla.bdnews24.com/politics/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'text'})

for r in r1:
    txt=r.find('a')['href']
    url=r.find('a').text[1:-1]
    news.append((url,txt,'Bdnews24'))

#-----------dhaka tribune------------

r=requests.get('https://bangla.dhakatribune.com/articles/politics')
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
print('POL',len(news))