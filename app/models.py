from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = slugify(self.name)
        super(Label, self).save(*args, **kwargs)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, editable=False, unique=True)
    content = models.TextField()
    pub_date = models.DateField()
    reporter = models.ForeignKey(User)
    labels = models.ManyToManyField(Label)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super(Article, self).save(*args, **kwargs)
