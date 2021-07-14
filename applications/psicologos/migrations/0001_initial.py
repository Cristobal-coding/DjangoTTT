# Generated by Django 3.2.2 on 2021-07-13 23:52

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=30, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=30, verbose_name='Apellido materno')),
                ('correo', models.CharField(max_length=50, unique=True, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=8, verbose_name='Telefono')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
            ],
            options={
                'verbose_name': 'Psicologo',
                'verbose_name_plural': 'Psicologos',
                'db_table': 'Psicologos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField(verbose_name='Fecha de emision')),
                ('pruebas_aplicadas', models.CharField(max_length=255, verbose_name='Pruebas aplicadas')),
                ('motivo', models.CharField(blank=True, max_length=255, verbose_name='Motivo')),
                ('comentario', models.CharField(blank=True, max_length=255, verbose_name='Comentario')),
                ('id_psicologo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informes', to='psicologos.psicologo')),
                ('rut_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informes', to='alumnos.alumno')),
            ],
            options={
                'verbose_name': 'Informe',
                'verbose_name_plural': 'Informes',
                'db_table': 'Informes',
                'ordering': ['-fecha_emision', '-id'],
            },
        ),
    ]
