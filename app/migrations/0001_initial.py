# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True,
                                        primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100,
                                          editable=False)),
                ('content', models.TextField()),
                ('pub_date', models.DateField()),
            ],
            options={
                'ordering': ('-pub_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True,
                                        primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='labels',
            field=models.ManyToManyField(to='app.Label'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
