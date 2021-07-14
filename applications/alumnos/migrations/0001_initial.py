# Generated by Django 3.2.2 on 2021-07-13 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('antecedentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, null=True, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=25, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=25, verbose_name='Apellido materno')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('sexo', models.CharField(choices=[('0', 'Femenino'), ('1', 'Masculino'), ('2', 'No especifica')], max_length=1, verbose_name='Sexo')),
                ('telefono', models.CharField(blank=True, max_length=8, null=True, verbose_name='Telefono')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Direccion')),
                ('estado', models.CharField(choices=[('0', 'Regular'), ('1', 'Abandonó'), ('2', 'Graduado')], max_length=1, verbose_name='estado')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'db_table': 'Alumnos',
                'ordering': ['apellido_paterno', 'apellido_materno'],
            },
        ),
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('rut', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True, verbose_name='Rut')),
                ('nombre_apoderado', models.CharField(max_length=50, verbose_name='Nombre apoderado')),
                ('apellido_paterno', models.CharField(max_length=25, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=25, verbose_name='Apellido materno')),
                ('telefono_apoderado', models.CharField(max_length=8, verbose_name='Telefono apoderado')),
                ('correo', models.CharField(max_length=20, unique=True, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Apoderado',
                'verbose_name_plural': 'Apoderados',
                'db_table': 'Apoderados',
                'ordering': ['nombre_apoderado', 'apellido_paterno'],
            },
        ),
        migrations.CreateModel(
            name='Alumno_antecedente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('detalle', models.CharField(blank=True, max_length=255)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno')),
                ('antecedente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='antecedentes.antecedente')),
            ],
            options={
                'db_table': 'Alumno_antecedente',
                'unique_together': {('alumno', 'antecedente')},
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='antecedentes',
            field=models.ManyToManyField(through='alumnos.Alumno_antecedente', to='antecedentes.Antecedente'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='rut_apoderado',
            field=models.ForeignKey(max_length=13, on_delete=django.db.models.deletion.CASCADE, related_name='alumnos', to='alumnos.apoderado'),
        ),
    ]
