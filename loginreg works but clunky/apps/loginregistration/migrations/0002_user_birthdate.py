# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginregistration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(default=1900),
            preserve_default=False,
        ),
    ]
