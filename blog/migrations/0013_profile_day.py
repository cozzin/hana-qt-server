# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-14 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180120_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='day',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7),
        ),
    ]