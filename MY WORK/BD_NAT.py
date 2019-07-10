import requests
#import text_summarization
from bs4 import BeautifulSoup
news=[]

r=requests.get('https://bdnews24.com/bangladesh/')
soup = BeautifulSoup(r.text, 'html.parser')

r1=soup.find_all('h3')

l=0
for r in r1:   #for h3 two news only
	if l<6:
	    txt=r.find('a')['href']
	    url=r.find('a').text[1:-1]
	    news.append((url,txt,"Bdnews24"))
	l+=1

print("BDNEWS BREAKING ",len(news)) 
for r in news:
	print(r[0]) 
