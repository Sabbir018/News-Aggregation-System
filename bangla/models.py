from django.db import models
from django.utils import timezone


class Most_read(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)


class Breaking_news(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)

class National(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)

class Politics(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)

class International(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)

class Sports(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)

class Entertainment(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)

class Technology(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    url = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    summary=models.CharField(max_length=2000)



