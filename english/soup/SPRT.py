import requests
from bs4 import BeautifulSoup
news=[]

#------------------Dailystar---------------
r=requests.get('https://www.thedailystar.net/sports')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'highlight-text'})
#r2=soup.find_all('a',attrs={'class':'sub-head margin-bottom-zero  color-green active'})
r2=soup.find_all('h5')

url='https://www.thedailystar.net'+r1[0].find('a')['href']
txt=r1[0].find('a').text
news.append((txt,url,"Dailystar"))
l=0
for r in r2:
	if l<4:
		url='https://www.thedailystar.net'+r.find('a')['href']
		txt=r.find('a').text
		news.append((txt,url,"Dailystar"))
	l+=1

#---------------Daily observer-------------------
r=requests.get('http://www.observerbd.com/cat.php?cd=185')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'title_inner'})

l=0
for r in r1:
	if l<5:
		txt=r.find('a').text
		url='http://www.observerbd.com/'+r.find('a')['href']
		news.append((txt,url,"observer"))
	l+=1
#-------------------------dhaka tribune-------------
r=requests.get('https://www.dhakatribune.com/articles/sport')
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

	
print("English sport",len(news))
