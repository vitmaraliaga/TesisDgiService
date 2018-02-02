# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-02 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tesis_proceso', '0002_auto_20171013_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisetapa',
            name='etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisetapas', to='proceso.Etapa', verbose_name='Etapa'),
        ),
        migrations.AlterField(
            model_name='tesisetapa',
            name='tesis_proceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tesisetapas', to='tesis_proceso.TesisProceso', verbose_name='Tesis_proceso'),
        ),
        migrations.AlterField(
            model_name='tesisproceso',
            name='proceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisprocesos', to='proceso.Proceso', verbose_name='Proceso'),
        ),
        migrations.AlterField(
            model_name='tesisrequisito',
            name='requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisitos', to='proceso.Requisito', verbose_name='Requisito'),
        ),
        migrations.AlterField(
            model_name='tesisrequisito',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisitos', to='proceso.Resultado', verbose_name='Resultado'),
        ),
        migrations.AlterField(
            model_name='tesisrequisito',
            name='tesis_tarea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisitos', to='tesis_proceso.TesisTarea', verbose_name='Tesis_tarea'),
        ),
        migrations.AlterField(
            model_name='tesisrequisitoarchivo',
            name='tesis_requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesisrequisitoarchivos', to='tesis_proceso.TesisRequisito', verbose_name='Tesis_requisito'),
        ),
        migrations.AlterField(
            model_name='tesistarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tesistareas', to='proceso.Tarea', verbose_name='Tarea'),
        ),
        migrations.AlterField(
            model_name='tesistarea',
            name='tesis_etapa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tesistareas', to='tesis_proceso.TesisEtapa', verbose_name='Tesis_etapa'),
        ),
    ]
