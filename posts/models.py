from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from users.models import UserProfile


class PostTag(models.Model):
    """
    Create tags for posts. Users should be able to add new tags.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PostCategory(models.Model):
    """
    Create categories for posts.
    Only admins should be able to add, edit or delete categories
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PostFlag(models.Model):
    """
    Create instance of PostFlag so users can flag posts for
    innappropriate or outdated content. Flags only visible to
    Library admins.
    """
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
    SUBMITTED = 'Submitted'
    PUBLISHED = 'Published'
    REVIEW = 'Review'
    STATUS_CHOICES = (
        (SUBMITTED, "Submitted"),
        (PUBLISHED, "Published"),
        (REVIEW, "Review"),
    )
    title = models.CharField(
        max_length=70,
        unique=True,
        error_messages={
            'unique': "This post title already exists, please choose another."
        })
    summary = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    body = RichTextField()
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='posts')
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=SUBMITTED)
    mod_message = models.TextField(max_length=300, null=True)
    moderator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True, blank=False,
        related_name='mod_field')
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.PROTECT,
        related_name="posts_to_category")
    tags = models.ManyToManyField(
        PostTag, related_name='post_tags', blank=True)
    likes = models.ManyToManyField(
        User, related_name='post_likes', blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name='post_bookmarks', blank=True)
    image_1 = models.ImageField(
        null=True, blank=True, upload_to="images/posts/")
    image_2 = models.ImageField(
        null=True, blank=True, upload_to="images/posts/")
    image_3 = models.ImageField(
        null=True, blank=True, upload_to="images/posts/")
    image_4 = models.ImageField(
        null=True, blank=True, upload_to="images/posts/")
    flag = models.ForeignKey(
        PostFlag,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='flags')
    editors_note = models.TextField(
        max_length=400, null=True, blank=True)

    def total_likes(self):
        """ Returns total likes a post has """
        return self.likes.count()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={'pk': self.pk, 'slug': self.slug})
