# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpdb_core', '0006_filelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='to_notify_email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
