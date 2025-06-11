from django.db import models
from api_papers.models import categories

class JournalsModel(models.Model):
    image = models.ImageField(upload_to='journals/', default="'profile pictures'/pic.png")
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(max_length=30, choices=categories)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    papers_id = models.ForeignKey('api_papers.PapersModel_UZ') # needs to be changed!
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()
