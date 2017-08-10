# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-10 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
                ('kind', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
