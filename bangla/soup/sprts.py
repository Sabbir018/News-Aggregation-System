import requests
from bs4 import BeautifulSoup
news=[]
#--------------prothom alo--------------
r=requests.get('http://www.prothomalo.com/sports')
soup = BeautifulSoup(r.text, 'html.parser')

r1=soup.find_all('div',attrs={'class':'col col1'})


l=0
for r in r1:
    if l<10:
        url='http://www.prothomalo.com/'+r.find('a')['href']
        t=r.find('h2')
        txt=t.find('span').text
        news.append((txt,url,'prothom alo'))
    l+=1

#----------------BDnenws------------

r=requests.get('https://bangla.bdnews24.com/sport/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'text'})

l=0
for r in r1:
    if l==6:
        break
    l+=1
    txt=r.find('a')['href']
    url=r.find('a').text[1:-1]
    news.append((url,txt,'Bdnews24'))
#print(len(news))

r=requests.get('https://www.jugantor.com/sports')
soup = BeautifulSoup(r.text, 'html.parser')
r2=soup.find_all('div',attrs={'class':"leadimg"})


l=0
for r in r2:
    if l==6:
        break
    l+=1
    url=r.find('a')['href']
    txt=r.find('a').text[2:-1]
    news.append((txt,url,'jugantor'))

print('sports',len(news))


