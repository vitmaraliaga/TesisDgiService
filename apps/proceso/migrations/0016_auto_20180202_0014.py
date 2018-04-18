# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-02 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0015_auto_20180202_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='proceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etapas', to='proceso.Proceso', verbose_name='Proceso'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='tarea_activador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='etapas_activador', to='proceso.Tarea', verbose_name='Tarea activador'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='tarea_desactivador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='etapas_desactivador', to='proceso.Tarea', verbose_name='Tarea desactivador'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularios', to='proceso.Tarea', verbose_name='Tarea'),
        ),
        migrations.AlterField(
            model_name='rolproceso',
            name='proceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rolprocesos', to='proceso.Proceso', verbose_name='Proceso'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='proceso.Etapa', verbose_name='Etapa'),
        ),
    ]