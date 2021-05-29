from django.db import models


class SlackChannel(models.Model):
    name = models.CharField(max_length=50)
    slack_channel_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
