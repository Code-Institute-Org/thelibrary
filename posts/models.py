from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import datetime

# Create your models here.
class Post(models.Model):
    """
    Create instance of Post
    """
    WAITING = 'Waiting'
    APPROVED = 'Approved'
    DEACTIVATED = 'Deactivated'
    STATUS_CHOICES = (
        (WAITING, "Awaiting Approval"),
        (APPROVED, "Approved"),
        (DEACTIVATED, "Deactivated")
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(default=datetime.date.today)
    updated_on = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=WAITING)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})