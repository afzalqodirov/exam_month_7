from django.db import models

# there are three models for three languages (UZ, RU, EN)
# so everyone can view and post in their own language
# For Uzbeks *different model, for Russians *different and for americans as well
categories = [
        ('0', 'AI'),
        ('1', 'Computer'),
        ('2', 'Marketing'),
        ('3', 'Product and consumption'),
        ('4', 'Shopping'),
        ('5', 'Brand')
        ]
class PapersModel_UZ(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='papers/', blank=True, null=True)
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(choices=categories, max_length=30)
    is_reviewed = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

    def __str__(self):return f'{self.author.username}:{self.title}'

    class Meta:
        db_table = 'papers_uz'
        unique_together = ('author', 'title')

class PapersModel_RU(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='papers/', blank=True, null=True)
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(choices=categories, max_length=30)
    is_reviewed = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

    def __str__(self):return f'{self.author.username}:{self.title}'

    class Meta:
        db_table = 'papers_ru'
        unique_together = ('author', 'title')

class PapersModel_EN(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='papers/', blank=True, null=True)
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(choices=categories, max_length=30)
    is_reviewed = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

    def __str__(self):return f'{self.author.username}:{self.title}'

    class Meta:
        db_table = 'papers_en'
        unique_together = ('author', 'title')
