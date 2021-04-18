from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.

class PostTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Create instance of Post
    """
    WAITING = 'Waiting'
    APPROVED = 'Approved'
    REVIEW = 'Review'
    STATUS_CHOICES = (
        (WAITING, "Awaiting Approval"),
        (APPROVED, "Approved"),
        (REVIEW, "Review"),
    )
    title = models.CharField(
        max_length=100,
        unique=True,
        error_messages={
            'unique':"This post title already exists, please choose another."
        }
    )
    summary = models.CharField(
        max_length=200,
        error_messages={
            'max_length': "Summary text is too long, please shorten to 200 characters or less."
        }
    )
    slug = models.SlugField(max_length=200, unique=True)
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_field')
    created_on = models.DateField(default=datetime.date.today)
    updated_on = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=WAITING)
    mod_message = models.TextField(max_length=300, null=True)
    moderator = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False, related_name='mod_field')
    likes = models.ManyToManyField(User, related_name='post_likes', null=True, blank=True)
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT, related_name="post_category")
    tags = models.ManyToManyField(PostTag, related_name='post_tags', null=True)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk, 'slug': self.slug})