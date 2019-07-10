# coding=utf-8
from django.shortcuts import render
from .models import Breaking_news,National,Sports,International,Technology,Politics,Entertainment,Most_read
from .soup import Brk_news,MSR,INT,NAT,POL,ENT,TEC,sprts


def about_us(request):
	return render(request, 'english/about.html', {})

def home(request):
	Most_read.objects.all().delete()
	#Most_read.objects.filter(url__contains=i[1])
	for i in MSR.news:
		bdn = Most_read()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]
		bdn.summary = "abc"
		bdn.save()

	pst= Most_read.objects.all()
	
	Breaking_news.objects.all().delete()	
	for i in Brk_news.news:
		bdn = Breaking_news()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = 'abc'

		bdn.save()
	post= Breaking_news.objects.all()	
	h1 = "Breaking news"
	h2="Most popular"	
	
	return render(request, 'bangla/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

def national(request):
	National.objects.all().delete()	
	for i in NAT.news:
		bdn = National()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = 'abc'
		bdn.save()
	post= National.objects.all()	
	h1 = "National news"
	h2="Breaking news"	

	pst= Breaking_news.objects.all()
	return render(request, 'bangla/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

def international(request):
	International.objects.all().delete()	
	for i in INT.news:
		bdn = International()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = 'abc'
		bdn.save()
	post= International.objects.all()	
	h1 = "International news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'bangla/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

def politics(request):
	Politics.objects.all().delete()	
	for i in POL.news:
		bdn = Politics()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = 'abc'
		bdn.save()
	post= Politics.objects.all()	
	h1 = "Politics news"
	h2="Breaking news"	

	pst= Breaking_news.objects.all()
	return render(request, 'bangla/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})


def entertainment(request):
	Entertainment.objects.all().delete()	
	for i in ENT.news:
		bdn = Entertainment()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = 'abc'
		bdn.save()
	post= Entertainment.objects.all()	
	h1 = "Entertainment news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'bangla/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})


def technology(request):
	Technology.objects.all().delete()	
	for i in TEC.news:
		bdn = Technology()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = 'abc'
		bdn.save()
	post= Technology.objects.all()	
	h1 = "Technology news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'bangla/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})



def sports(request):
	Sports.objects.all().delete()	
	for i in sprts.news:
		bdn = Sports()
		bdn.author=i[2]
		bdn.title=i[0]
		bdn.url=i[1]		
		bdn.summary = 'abc'
		bdn.save()
	post= Sports.objects.all()	
	h1 = "Sports news"
	h2="Breaking news"	
	pst= Breaking_news.objects.all()
	return render(request, 'bangla/demo.html', {'h1':h1,'h2':h2,'post':post,'pst':pst})

