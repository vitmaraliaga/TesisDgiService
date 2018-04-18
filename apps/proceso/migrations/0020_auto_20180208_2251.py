# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0019_auto_20180208_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampoValidation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('data', models.CharField(blank=True, max_length=200, null=True, verbose_name='Data')),
                ('campo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proceso.Campo', verbose_name='Campo')),
            ],
            options={
                'verbose_name': 'CampoValidation',
                'verbose_name_plural': 'CampoValidations',
                'ordering': ('campo',),
            },
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('key', models.CharField(max_length=50, verbose_name='Key')),
            ],
            options={
                'verbose_name': 'validation',
                'verbose_name_plural': 'validations',
            },
        ),
        migrations.AddField(
            model_name='campovalidation',
            name='validation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proceso.Validation', verbose_name='Validation'),
        ),
    ]