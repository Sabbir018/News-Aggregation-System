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



print("BDNEWS BREAKING ",len(news)) 
for r in news:
	print(r[0]) 
