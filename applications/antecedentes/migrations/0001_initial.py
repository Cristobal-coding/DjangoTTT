# Generated by Django 3.2.2 on 2021-07-25 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_antecedente', models.CharField(max_length=50, verbose_name='Nombre antecedente')),
            ],
            options={
                'verbose_name': 'Antecedente',
                'verbose_name_plural': 'Antecedentes',
                'db_table': 'Antecedentes',
                'ordering': ['id'],
            },
        ),
    ]
