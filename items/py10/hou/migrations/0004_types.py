# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hou', '0003_auto_20180622_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pid', models.IntegerField()),
                ('path', models.CharField(max_length=50)),
            ],
        ),
    ]