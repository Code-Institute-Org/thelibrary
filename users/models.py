from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)
    date_joined = models.DateField(default=datetime.date.today)

    def __str__(self):
        
        status = '*mod' if self.is_mod else ''
        if self.is_admin: status = '*admin'

        return f'{self.user.username} {status} | {self.date_joined}'