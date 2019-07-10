from django.shortcuts import render
from django.utils import timezone

from .models import Bdnews,Sports,Entertainment,Technology,Politics,Dailystar
from .soup import bdnewsDesh,BdSports,JugantorSports,JugantorDesh,BdnewsProjukti,KalerkonthProjukti,BdnewsRajnity,DS,text_summarization
from .data import SPORTS

# Create your views here.



def index(request):
    Bdnews.objects.all().delete()
    for i in range(5):
        bdn=Bdnews()
        bdn.title = bdnewsDesh.news[i][0]
        bdn.url = bdnewsDesh.news[i][1]
        bdn.time = timezone.now()
        bdn.save()

        jgn = Bdnews()
        jgn.title = JugantorDesh.news[i][0]
        jgn.url = JugantorDesh.news[i][1]
        jgn.time = timezone.now()
        jgn.save()
    post = Bdnews.objects.all()
    return render(request, 'web/Bnews.html', {'post': post})


def sports(request):

    SPORTS()

    post = Sports.objects.all()
    return render(request, 'web/Bnews.html', {'post': post})

def technology(request):
    Technology.objects.all().delete()

    for i in range(5):
        bdn=Technology()
        bdn.title = BdnewsProjukti.news[i][0]
        bdn.url = BdnewsProjukti.news[i][1]
        bdn.time = timezone.now()
        bdn.author = 'Bdnews'
        bdn.save()

        jgn = Technology()
        jgn.title = KalerkonthProjukti.news[i][0]
        jgn.url = KalerkonthProjukti.news[i][1]
        jgn.time = timezone.now()
        jgn.author = 'kalerkontho'
        jgn.save()



    post = Technology.objects.all()
    return render(request, 'web/Bnews.html', {'post': post})

def politics(request):
    Politics.objects.all().delete()

    for i in range(5):
        bdn=Politics()
        bdn.title = BdnewsRajnity.news[i][0]
        bdn.url = BdnewsRajnity.news[i][1]
        bdn.time = timezone.now()
        bdn.author = 'Bdnews'
        bdn.save()

    post = Politics.objects.all()
    return render(request, 'web/Bnews.html', {'post': post})


def dailystar(request):
    Dailystar.objects.all().delete()

    for i in range(2):
        ds=Dailystar()
        u=DS.news[i][0]
        sm=text_summarization.summarizeURL(u,2)
        ds.title = DS.news[i][1]
        ds.url = DS.news[i][0]
        ds.time = timezone.now()
        ds.author = 'Bdnews'
        ds.summury=sm
        ds.save()

    post = Dailystar.objects.all()

    return render(request, 'web/dailystar.html', {'post': post})
























