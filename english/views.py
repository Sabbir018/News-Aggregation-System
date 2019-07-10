# coding=utf-8
from django.shortcuts import render
from .models import Breaking_news,National,Sports,International,Technology,Politics,Entertainment,Most_read
from .soup import ENG_BREAK,MSR,text_summarization,INT,NAT,POL,ENT,TEC,SPRT


def about(request):
	return render(request, 'english/about.html', {})

def demo():
	Most_read.objects.all().delete()
	for i in MSR.news:
		bdn = Most_read()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]
		bdn.summary = "abc"
		bdn.save()

	post= Most_read.objects.all()
	return post

def home(request):
	Breaking_news.objects.all().delete()	
	for i in ENG_BREAK.news:
		bdn = Breaking_news()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = text_summarization.summarizeURL(i[1],2)

		bdn.save()
	post= Breaking_news.objects.all()	
	h1 = "Breaking news"
	h2="Most popular"	
	pst= demo()
	return render(request, 'english/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

def national(request):
	National.objects.all().delete()	
	for i in NAT.news:
		bdn = National()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = text_summarization.summarizeURL(i[1],1)
		bdn.save()
	post= National.objects.all()	
	h1 = "National news"
	h2="Breaking news"	

	pst= Breaking_news.objects.all()
	return render(request, 'english/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

def international(request):
	International.objects.all().delete()	
	for i in INT.news:
		bdn = International()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = text_summarization.summarizeURL(i[1],1)
		bdn.save()
	post= International.objects.all()	
	h1 = "International news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'english/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

def politics(request):
	Politics.objects.all().delete()	
	for i in POL.news:
		bdn = Politics()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = text_summarization.summarizeURL(i[1],1)
		bdn.save()
	post= Politics.objects.all()	
	h1 = "Politics news"
	h2="Breaking news"	

	pst= Breaking_news.objects.all()
	return render(request, 'english/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})


def entertainment(request):
	Entertainment.objects.all().delete()	
	for i in ENT.news:
		bdn = Entertainment()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = text_summarization.summarizeURL(i[1],1)
		bdn.save()
	post= Entertainment.objects.all()	
	h1 = "Entertainment news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'english/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})


def technology(request):
	Technology.objects.all().delete()	
	for i in TEC.news:
		bdn = Technology()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = text_summarization.summarizeURL(i[1],1)
		bdn.save()
	post= Technology.objects.all()	
	h1 = "Technology news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'english/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})



def sports(request):
	Sports.objects.all().delete()	
	for i in SPRT.news:
		bdn = Sports()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = text_summarization.summarizeURL(i[1],1)
		bdn.save()
	post= Sports.objects.all()	
	h1 = "Sports news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'english/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

