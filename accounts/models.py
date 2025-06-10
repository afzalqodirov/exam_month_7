from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_reviewer = models.BooleanField(default=False)
    scientific_degree = models.TextField(null=True, blank=True)
    extra_info = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='profile pictures/', default='profile pictures/default.png')
    organization = models.TextField(null=True, blank=True)
