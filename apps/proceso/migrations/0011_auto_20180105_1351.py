# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-05 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0010_auto_20180105_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='key',
            field=models.CharField(help_text='Este campo es único', max_length=100, verbose_name='Key'),
        ),
    ]