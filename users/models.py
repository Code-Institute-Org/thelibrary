from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime


class UserProfile(models.Model):
    """
    Extends User model to track admin/mod/staff status, store social links,
    bio and date joined. Instance of UserProfile is automatically generated
    on creation of a new User account.
    """
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profiles/",
        default="/images/profiles/default-profile-pic.png")
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
        if self.is_admin:
            status = ' *admin'
        elif self.is_mod:
            status = ' *mod'
        else:
            status = ''

        return f'{self.user.username}{status} | {self.date_joined}'

    def kudos_badge(self):
        """
        Returns string value to be used as class name in html,
        this class name controls the background color of the badge
        If author has no kudos badge yet, the 'invisible' class
        returned will hide it.
        """
        total_posts = self.posts.filter(status="Published").count()

        if total_posts >= 15:
            return 'kudos-badge-gold'
        elif total_posts >= 8:
            return 'kudos-badge-silver'
        elif total_posts >= 3:
            return 'kudos-badge-bronze'
        else:
            return 'invisible'

    def get_author_name(self):
        """
        Method to return users full name if provided,
        if not it returns their username
        """
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Creates UserProfile on new instance of User """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ Saves instance of UserProfile """
    instance.userprofile.save()
