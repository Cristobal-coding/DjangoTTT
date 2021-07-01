# Generated by Django 3.2.2 on 2021-07-01 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('cod_asign', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True, verbose_name='Cod_asign')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
                'db_table': 'Asignaturas',
                'ordering': ['nombre'],
            },
        ),
    ]
