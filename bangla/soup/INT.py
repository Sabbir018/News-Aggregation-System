import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('http://www.prothomalo.com/international')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'col col1'})

l=0
for r in r1:
	
		url='http://www.prothomalo.com/'+r.find('a')['href']
		t=r.find('h2')
		txt=t.find('span').text
		news.append((txt,url,'prothom alo'))



r=requests.get('https://www.jugantor.com/international')
soup = BeautifulSoup(r.text, 'html.parser')
r2=soup.find_all('div',attrs={'class':"leadmorehl2"})
l=0
for r in r2:
	if l<10:	
	    url=r.find('a')['href']
	    txt=r.find('a').text
	    news.append((txt,url,'Jugantor'))
	l+=1


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
   

print('INT',len(news))