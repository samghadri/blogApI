# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_userprofileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='exit', unique=True),
            preserve_default=False,
        ),
    ]
