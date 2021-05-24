# Generated by Django 3.2.2 on 2021-05-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellido_materno',
            field=models.CharField(max_length=25, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido_paterno',
            field=models.CharField(max_length=25, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='estado',
            field=models.CharField(choices=[('0', 'Regular'), ('1', 'Abandonó'), ('2', 'Finalizado')], max_length=1, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=8, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='apoderado',
            name='apellido_materno',
            field=models.CharField(max_length=25, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='apoderado',
            name='apellido_paterno',
            field=models.CharField(max_length=25, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='apoderado',
            name='telefono_apoderado',
            field=models.CharField(max_length=8, verbose_name='Telefono apoderado'),
        ),
    ]
