# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-12 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripcion')),
                ('url', models.CharField(blank=True, default='#', max_length=50, null=True, verbose_name='Url')),
                ('icono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Icono')),
                ('activo', models.DateField(default=True, verbose_name='Activo')),
                ('nivel', models.CharField(choices=[('1', 'Primer nivel'), ('2', 'Segundo nivel'), ('3', 'Tercer nivel')], default='1', max_length=1, verbose_name='Nivel')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos', to='config.Menu', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellido_paterno', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1, verbose_name='Apellido materno')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('direccion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, max_length=12, null=True, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, max_length=12, null=True, verbose_name='Celular')),
                ('num_doc', models.CharField(blank=True, help_text='Número de documento nacional de identidad', max_length=8, null=True, unique=True, verbose_name='Dni')),
                ('carnet_extrangeria', models.CharField(blank=True, help_text='Número de carnet de extrangería', max_length=12, null=True, verbose_name='Carnet de extrangería')),
                ('foto', models.ImageField(default='personas/fotos/none/default.png', upload_to='persona/fotos/', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]