# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0003_auto_20180227_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
    ]