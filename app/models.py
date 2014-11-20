from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField()
    reporter = models.ForeignKey(User)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)