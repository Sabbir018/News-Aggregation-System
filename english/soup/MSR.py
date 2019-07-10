import requests
from bs4 import BeautifulSoup
news=[]

#-----------for thedailystar-----------------
r=requests.get('https://www.thedailystar.net/#')
soup = BeautifulSoup(r.text, 'html.parser')

r2=soup.find_all('ul',attrs={'class':'list-type-bullet more-stories-list'})

i=0
for r in r2:
    if i<4:
    	r=r.find('h5')
    	txt=r.find('a').text
    	url='https://www.thedailystar.net'+r.find('a')['href']
    	#print(url)
    	news.append((txt, url,'Dailystar'))
    i+=1


#-----------for thedaily observer-----------------
r=requests.get('http://www.observerbd.com/index.php')
soup = BeautifulSoup(r.text, 'html.parser')

r2=soup.find_all('div',attrs={'class':'bullte_latest'})

i=0
for r in r2:
    if i>2 and i<8:
    	txt=r.find('a').text
    	url='http://www.observerbd.com/'+r.find('a')['href']
        
    	news.append((txt, url,'Observer'))
    i+=1



