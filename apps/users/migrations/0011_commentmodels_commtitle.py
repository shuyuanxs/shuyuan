# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180110_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodels',
            name='commtitle',
            field=models.CharField(default='', max_length=20, verbose_name='评论标题'),
        ),
    ]
