# Generated by Django 3.2.2 on 2021-07-25 18:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('rut', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(blank=True, max_length=30, null=True, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(blank=True, max_length=30, null=True, verbose_name='Apellido materno')),
                ('correo', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=8, null=True, verbose_name='Telefono')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
            ],
            options={
                'verbose_name': 'Psicologo',
                'verbose_name_plural': 'Psicologos',
                'db_table': 'Psicologos',
                'ordering': ['rut'],
            },
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField(verbose_name='Fecha de emision')),
                ('pruebas_aplicadas', ckeditor.fields.RichTextField(null=True)),
                ('motivo', ckeditor.fields.RichTextField(null=True)),
                ('comentario', ckeditor.fields.RichTextField(null=True)),
                ('rut_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informes', to='alumnos.alumno')),
                ('rut_psicologo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informes', to='psicologos.psicologo')),
            ],
            options={
                'verbose_name': 'Informe',
                'verbose_name_plural': 'Informes',
                'db_table': 'Informes',
                'ordering': ['-fecha_emision', '-id'],
            },
        ),
    ]
