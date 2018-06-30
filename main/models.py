from django.db import models
from django.utils import timezone


class Draw(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image_url = models.CharField(max_length=1000)
    share_url = models.CharField(max_length=1000)
    likes = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}, L#{}".format(self.title, self.likes)


class Dance(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image_url = models.CharField(max_length=1000)
    video_url = models.CharField(max_length=1000)
    share_url = models.CharField(max_length=1000)
    views = models.IntegerField()
    likes = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} V#{}, L#{}".format(self.title, self.views, self.likes)