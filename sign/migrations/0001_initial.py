# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-03-23 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('baseurl', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('args', models.CharField(max_length=1000)),
                ('method', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
