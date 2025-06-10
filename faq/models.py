from django.db import models

class FAQModel(models.Model):
    question = models.TextField()
    answer = models.TextField()
