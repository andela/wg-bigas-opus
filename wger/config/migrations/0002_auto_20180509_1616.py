# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-09 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymconfig',
            name='default_gym',
            field=models.ForeignKey(blank=True, help_text='Select the default gym for                                                  this installation. This will assign all new                                                  registered users to this gym and update all existing                                                  users without a gym.', null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Gym', verbose_name='Default gym'),
        ),
        migrations.AlterField(
            model_name='languageconfig',
            name='item',
            field=models.CharField(choices=[('1', 'Exercises'), ('2', 'Ingredients')], editable=False, max_length=2),
        ),
    ]
