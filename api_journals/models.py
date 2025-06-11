from django.db import models
from api_papers.models import categories

class JournalsModel_UZ(models.Model):
    image = models.ImageField(upload_to='journals/', default="'profile pictures'/pic.png")
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(max_length=30, choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

class JournalsModel_RU(models.Model):
    image = models.ImageField(upload_to='journals/', default="'profile pictures'/pic.png")
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(max_length=30, choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

class JournalsModel_EN(models.Model):
    image = models.ImageField(upload_to='journals/', default="'profile pictures'/pic.png")
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(max_length=30, choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()
