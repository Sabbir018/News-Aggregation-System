import requests
from bs4 import BeautifulSoup
news=[]


#-----------------------for dhakatribune------------
r=requests.get('https://www.dhakatribune.com/articles/bangladesh/')
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

#------------------for obserber--------------------------

r=requests.get('http://www.observerbd.com/cat.php?cd=186')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'title_inner'})

l=0
for r in r1:   #for h3 two news only
	if l<6:
	    txt='http://www.observerbd.com/'+r.find('a')['href']
	    t=r.find('a')
	    url=r.find('b').text
	    news.append((url,txt,"observer"))
	    
	l+=1

print("BDNEWS BREAKING ",len(news)) 
