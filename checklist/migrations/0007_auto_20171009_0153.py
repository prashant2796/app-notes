# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-08 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_auto_20171008_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='task_text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.DeleteModel(
            name='Todotext',
        ),
    ]
