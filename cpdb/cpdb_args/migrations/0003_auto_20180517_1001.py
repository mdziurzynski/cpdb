# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpdb_args', '0002_auto_20180516_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='argprimerpair',
            name='name',
        ),
        migrations.RemoveField(
            model_name='argprimerpair',
            name='primer_for_seq',
        ),
        migrations.RemoveField(
            model_name='argprimerpair',
            name='primer_rev_seq',
        ),
        migrations.AddField(
            model_name='argprimerpair',
            name='file_line_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='argprimerpair',
            name='elongation_time',
            field=models.CharField(max_length=10),
        ),
    ]
