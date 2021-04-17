from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.
class Post(models.Model):
    """
    Create instance of Post
    """
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=datetime.date.today)
    date_last_updated = models.DateField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"