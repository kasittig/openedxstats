# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-25 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_sitesummarysnapshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='is_private_instance',
            field=models.BooleanField(default=False),
        ),
    ]
