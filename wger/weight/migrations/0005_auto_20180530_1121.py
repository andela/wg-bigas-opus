# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-30 08:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0004_auto_20180530_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightentry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='User'),
        ),
    ]