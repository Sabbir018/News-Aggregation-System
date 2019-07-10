import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.jugantor.com/national')
soup = BeautifulSoup(r.text, 'html.parser')
r2=soup.find_all('div',attrs={'class':"leadmorehl2"})

news=[]
l=0
for r in r2:
    if l==6:
        break

    l+=1
    url=r.find('a')['href']
    txt=r.find('a').text
    news.append((txt,url,'Jugantor'))

#print(len(news))


r=requests.get('https://bangla.bdnews24.com/samagrabangladesh/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('h6',attrs={'class':'default'})
r2=soup.find_all('h1',attrs={'class':'default'})

r01=r1+r2

l=0
for r in r01:
    if l==5:
        break
    l+=1
    url=r.find('a')['href']
    txt=r.find('a').text[1:-1]
    news.append((txt,url,'Bdnews24'))
#------------------dhaka tribune---------------
r=requests.get('https://bangla.dhakatribune.com/articles/bangladesh')
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
print('NAT',len(news))