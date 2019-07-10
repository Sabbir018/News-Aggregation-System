from django.urls import path
from . import views


urlpatterns = [
   	path('home/',views.home,name="english/home"),
    path('national/', views.national, name="english/national"),
    path('sports/',views.sports,name="english/sports"),
    path('politics/', views.politics, name="english/politics"),
    path('technology/', views.technology, name="english/technology"),
    path('entertainment/', views.entertainment, name="english/entertainment"),
    path('international/', views.international, name="english/international"),
    
    path('about_us/',views.about, name='english/about'),


]
