from django.contrib.auth.models import User
from django.db import models

from articleapp.models import Article


# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)

    create_at = models.DateTimeField(auto_now=True)