from django.db import models

categories = [
        ('0', 'AI'),
        ('1', 'Computer'),
        ('2', 'Marketing'),
        ('3', 'Product and consumption'),
        ('4', 'Shopping'),
        ('5', 'Brand')
        ]
class PapersModel(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='papers/', blank=True, null=True)
    title = models.CharField(max_length=200)
    article = models.TextField()
    reference = models.CharField(choices=categories, max_length=30)
    is_reviewed = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

    def __str__(self):return self.title

    class Meta:
        db_table = 'papers'
        unique_together = ('author', 'title')
