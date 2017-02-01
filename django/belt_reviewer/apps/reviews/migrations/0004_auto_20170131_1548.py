# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_review_review_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_title',
        ),
        migrations.AddField(
            model_name='review',
            name='review_text',
            field=models.CharField(default='Excellent book', max_length=2500),
            preserve_default=False,
        ),
    ]
