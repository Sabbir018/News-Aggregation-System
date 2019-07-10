import requests
from bs4 import BeautifulSoup

r=requests.get('http://web.dailyjanakantha.com/online-science/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'list-article smp-listart'})

news=[]
l=0

for r in r1:
    if l==10:
        break
    l+=1
    url=r.find('a')['href']
    txt=r.find('h2').text
    news.append((txt,url,'janakantha'))


r=requests.get('https://bangla.bdnews24.com/science/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('h1',attrs={'class':'default'})
r2=soup.find_all('div',attrs={'class':'text'})

for r in r2:
    txt=r.find('a')['href']
    url=r.find('a').text[1:-1]
    news.append((url,txt,'Bdnews24'))

#-------------------dhaka tribune
r=requests.get('https://bangla.dhakatribune.com/articles/tech')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'top-news-cont list-para'})
r2=soup.find_all('h4',attrs={'class':'news-title'})

t=[]
u=[]
l=0
for r in r1:
	if l<6:
		url='https://www.dhakatribune.com'+r.find('a')['href']
		u.append(url)

l=0
for r in r2:
	if l<6:
		txt=r.text[1:-1]
		t.append(txt)

for i in range(6):
	news.append((t[i],u[i],'Dhakatribune'))
print('TEC',len(news))