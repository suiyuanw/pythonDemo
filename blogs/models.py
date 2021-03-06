import pytz as pytz
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """docstring for Post"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def to_dict(self):
        localtz = pytz.timezone('Asia/Shanghai')
        return {
            'id': self.id,
            'author': self.author.username,
            'title': self.title,
            'text': self.text,
            'created_date': self.created_date.astimezone(localtz).strftime(
                "%Y.%m.%d %H:%M") if self.created_date else '',
            'published_date': self.published_date.astimezone(localtz).strftime(
                "%Y.%m.%d %H:%M") if self.published_date else '',
        }
