# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-26 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadFile',
            fields=[
                ('filename', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('filedescription', models.CharField(max_length=256)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
