# Generated by Django 3.2.2 on 2021-07-04 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asignaturas', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.asignatura')),
            ],
            options={
                'db_table': 'Asignatura_Plan',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='ID_Curso')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('electivo', models.CharField(blank=True, choices=[('EL', 'Electricidad'), ('MET', 'Construcciones metálicas.'), ('CON', 'Construccion')], max_length=5, null=True, verbose_name='Electivos')),
                ('numero', models.FloatField(verbose_name='Numero')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'Cursos',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellido_paterno', models.CharField(max_length=30, verbose_name='A.Paterno')),
                ('apellido_materno', models.CharField(max_length=30, verbose_name='A.Materno')),
                ('asig_impartir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignatura', to='asignaturas.asignatura')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'db_table': 'Profesores',
                'ordering': ['nombres'],
            },
        ),
        migrations.CreateModel(
            name='PlanEstudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('detalle_url', models.CharField(max_length=255, verbose_name='Url')),
                ('asignaturas', models.ManyToManyField(through='cursos.Asignatura_Plan', to='asignaturas.Asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('cod_fecha', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Cod_fecha')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_termino', models.DateField(blank=True, null=True, verbose_name='Fecha de Termino')),
                ('semestres', models.CharField(choices=[('1', 'Primer semestre'), ('2', 'Segundo semestre')], max_length=3, verbose_name='Semestre')),
                ('year', models.IntegerField(verbose_name='Año')),
            ],
            options={
                'verbose_name': 'Fecha',
                'verbose_name_plural': 'Fechas',
                'db_table': 'Fechas',
                'ordering': ['-year', '-semestres'],
                'unique_together': {('semestres', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Curso_Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_current', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
            ],
            options={
                'db_table': 'Curso_Alumno',
                'unique_together': {('curso', 'alumno')},
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(related_name='cursos', through='cursos.Curso_Alumno', to='alumnos.Alumno'),
        ),
        migrations.AddField(
            model_name='curso',
            name='cod_fecha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='cursos.fecha'),
        ),
        migrations.AddField(
            model_name='curso',
            name='id_prof_jefe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jefe', to='cursos.profesor'),
        ),
        migrations.AddField(
            model_name='curso',
            name='plan_estudio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='cursos.planestudio'),
        ),
        migrations.AddField(
            model_name='asignatura_plan',
            name='id_profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesor', to='cursos.profesor'),
        ),
        migrations.AddField(
            model_name='asignatura_plan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.planestudio'),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together={('id_curso', 'cod_fecha')},
        ),
        migrations.AlterUniqueTogether(
            name='asignatura_plan',
            unique_together={('plan', 'asignatura')},
        ),
    ]
