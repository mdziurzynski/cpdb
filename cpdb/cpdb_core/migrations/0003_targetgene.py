# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpdb_core', '0002_antibioticclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetGene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('antibiotic_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpdb_core.AntibioticClass')),
            ],
        ),
    ]
