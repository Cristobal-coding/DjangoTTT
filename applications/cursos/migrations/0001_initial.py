# Generated by Django 3.2.2 on 2021-07-01 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0002_alter_alumno_options'),
        ('asignaturas', '0001_initial'),
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
                ('letra', models.CharField(max_length=1, verbose_name='Letra')),
                ('electivo', models.CharField(blank=True, choices=[('EL', 'Electricidad'), ('MET', 'Construcciones metálicas.'), ('CON', 'Construccion')], max_length=5, null=True, verbose_name='Electivos')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'Cursos',
                'ordering': ['nombre'],
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
                ('año', models.CharField(choices=[('0', '2021'), ('1', '2020'), ('2', '2019'), ('3', '2018'), ('4', '2017'), ('5', '2016'), ('6', '2015'), ('7', '2014'), ('8', '2013'), ('9', '2012'), ('10', '2011'), ('11', '2010'), ('12', '2009'), ('13', '2008'), ('14', '2007'), ('15', '2006'), ('16', '2005'), ('17', '2004'), ('18', '2003'), ('19', '2002'), ('20', '2001'), ('21', '2000')], max_length=4, verbose_name='Año')),
            ],
            options={
                'verbose_name': 'Fecha',
                'verbose_name_plural': 'Fechas',
                'db_table': 'Fechas',
                'unique_together': {('semestres', 'año')},
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
            field=models.ManyToManyField(through='cursos.Curso_Alumno', to='alumnos.Alumno'),
        ),
        migrations.AddField(
            model_name='curso',
            name='cod_fecha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fecha', to='cursos.fecha'),
        ),
        migrations.AddField(
            model_name='curso',
            name='id_prof_jefe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jefe', to='cursos.profesor'),
        ),
        migrations.AddField(
            model_name='curso',
            name='plan_estudio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='cursos.planestudio'),
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
