# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Freela',
            new_name='Job',
        ),
        migrations.RenameModel(
            old_name='Freelancer',
            new_name='Person',
        ),
        migrations.AlterModelTable(
            name='job',
            table='freela_freela',
        ),
        migrations.AlterModelTable(
            name='person',
            table='freela_freelancer',
        ),
    ]
