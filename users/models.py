from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post

import datetime

# Create your models here.

class UserProfile(models.Model):
    """
    Extends User model to track admin/mod status. Is automatically generated
    on creation of a new User account.
    """
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profiles/")
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(default=datetime.date.today)

    def __str__(self):
        """
        Returns usable string for admin panel,
        highlights if user is admin or mod
        """
        status = '*mod' if self.is_mod else ''
        if self.is_admin: status = '*admin'

        return f'{self.user.username} {status} | {self.date_joined}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()