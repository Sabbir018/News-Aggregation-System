import requests
from bs4 import BeautifulSoup
news=[]

r=requests.get('http://www.prothomalo.com/entertainment')
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

#--------bdnews-----------------

r=requests.get('https://bangla.bdnews24.com/glitz/')
soup = BeautifulSoup(r.text, 'html.parser')
r1=soup.find_all('div',attrs={'class':'text'})


l=0


for r in r1:
    if l==10:
        break
    txt=r.find('a')['href']
    url=r.find('a').text[1:-1]
    news.append((url,txt,'Bdnews24'))
    l+=1

print("Entertainment",len(news))

