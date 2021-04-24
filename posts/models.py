from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime

from users.models import UserProfile

# Create your models here.

class PostTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PostFlag(models.Model):
    INNAPPROPRIATE = 'Innappropriate content'
    OUTDATED = 'Outdated content'
    FLAG_REASONS = (
        (INNAPPROPRIATE, "Innappropriate content"),
        (OUTDATED, "Outdated content"),
    )
    flagger = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        related_name='post_flagger'
    )
    reason = models.CharField(
        max_length=100,
        choices=FLAG_REASONS,
        default=INNAPPROPRIATE
    )
    def __str__(self):
        return f"flag by {self.flagger} | {self.reason}"

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
    summary = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = RichTextField()
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='posts'
    )
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=WAITING
    )
    mod_message = models.TextField(max_length=300, null=True)
    moderator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        related_name='mod_field'
    )
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.PROTECT,
        related_name="post_category"
    )
    tags = models.ManyToManyField(
        PostTag, related_name='post_tags', blank=True
    )
    likes = models.ManyToManyField(
        User, related_name='post_likes', blank=True
    )
    bookmarks = models.ManyToManyField(
        User, related_name='post_bookmarks', blank=True
    )
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/posts/")
    image_2 = models.ImageField(null=True, blank=True, upload_to="images/posts/")
    image_3 = models.ImageField(null=True, blank=True, upload_to="images/posts/")
    image_4 = models.ImageField(null=True, blank=True, upload_to="images/posts/")
    flag = models.ForeignKey(
        PostFlag,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='flags'
    )
    editors_note = models.TextField(max_length=400, null=True, blank=True)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk, 'slug': self.slug})

