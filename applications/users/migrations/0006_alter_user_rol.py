# Generated by Django 3.2.2 on 2021-06-07 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210605_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='users.rol'),
        ),
    ]
