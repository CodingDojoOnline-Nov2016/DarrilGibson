# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginregistration', '0002_user_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
    ]
