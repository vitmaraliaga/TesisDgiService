# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-12 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorInvestigacion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'DirectorInvestigacion',
                'verbose_name_plural': 'DirectorInvestigaciones',
            },
        ),
        migrations.CreateModel(
            name='DirectorInvestigacionEscuela',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='Fecha de finalización')),
                ('director_investigacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.DirectorInvestigacion')),
            ],
            options={
                'verbose_name': 'DirectorInvestigacionEscuela',
                'verbose_name_plural': 'DirectorInvestigacionEscuelas',
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('alias', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alias')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('logo', models.ImageField(default='escuela/logos/none/default.png', upload_to='escuela/logos/', verbose_name='Logo')),
                ('mision', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Misión')),
                ('vision', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Vision')),
            ],
            options={
                'verbose_name': 'Escuela',
                'verbose_name_plural': 'Escuelas',
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('alias', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alias')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('logo', models.ImageField(default='escuela/logos/none/default.png', upload_to='escuela/logos/', verbose_name='Logo')),
                ('tema', models.CharField(default='default-theme', max_length=20, verbose_name='Tema')),
                ('mision', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Misión')),
                ('vision', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Visión')),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.CreateModel(
            name='LineaInvestigacion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'LineaInvestigacion',
                'verbose_name_plural': 'LineaInvestigacions',
            },
        ),
        migrations.AddField(
            model_name='escuela',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escuela', to='academico.Facultad', verbose_name='Facultad'),
        ),
        migrations.AddField(
            model_name='directorinvestigacionescuela',
            name='escuela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Escuela'),
        ),
        migrations.AddField(
            model_name='directorinvestigacion',
            name='escuela',
            field=models.ManyToManyField(through='academico.DirectorInvestigacionEscuela', to='academico.Escuela'),
        ),
        migrations.AddField(
            model_name='directorinvestigacion',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='config.Persona', verbose_name='Persona'),
        ),
    ]