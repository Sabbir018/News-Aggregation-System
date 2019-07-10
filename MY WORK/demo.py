import requests
from bs4 import BeautifulSoup
news=[]


r=requests.get('https://bangla.bdnews24.com/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'text'})
r2=soup.find_all('h6',attrs={'class':'default'})



url=r1[0].find('a')['href']
txt=r1[0].find('a').text[1:-1]
news.append((txt,url,'Bdnews24'))

for r in r2:
    txt=r.find('a')['href']
    url=r.find('a').text[1:-1]
    news.append((url,txt,"Bdnews24"))
   
