from django.db import models

class MessagesModel(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    # the email field might be null but in any case the user field has email field which is REQUIRED
    # this was added in case the user want to recieve message to another email address
    email = models.EmailField(null=True, blank=True)

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)

    def __str__(self):return f'{self.user.username}: {self.message}'
    
    class Meta:
        db_table = 'messages'
