# Generated by Django 3.2.2 on 2021-06-06 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_rol_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RemoveField(
            model_name='rol',
            name='activo',
        ),
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(error_messages={'unique': 'Ya existe un rol con este Nombre.'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(blank=True, error_messages={'unique': 'Este Rut ya esta Registrado.'}, max_length=13, unique=True, verbose_name='Rut'),
        ),
    ]
