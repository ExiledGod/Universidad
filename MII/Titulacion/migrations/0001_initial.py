# Generated by Django 2.1.2 on 2019-06-07 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumno', '0009_auto_20190605_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno_en_titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellp', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('apellm', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('rut', models.CharField(max_length=50, verbose_name='Rut')),
                ('mail', models.EmailField(max_length=254, verbose_name='Mail')),
            ],
            options={
                'verbose_name': 'Alumno_Titulacion',
                'verbose_name_plural': 'Alumnos_Titulaciones',
                'ordering': ('nombre', 'apellp', 'apellm', 'rut', 'mail', 'estado_anterior', 'estado_actual', 'fk_idcomite', 'avance', 'entreegafinal'),
            },
        ),
        migrations.CreateModel(
            name='avanceTesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='comite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='director_tesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dirTesis_name', models.CharField(max_length=50)),
                ('dirTesis_apllM', models.CharField(max_length=50)),
                ('dirTesis_apllP', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EntregaTesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=50, verbose_name='Calificacion')),
                ('comentario', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='EntregaTesisFinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('fk_entregaTesis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.EntregaTesis')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('valido', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Actual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Anterior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='ProfExaminador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellm', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('apellp', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('mail', models.EmailField(max_length=254)),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
            ],
        ),
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Tesis')),
                ('archivo', models.FileField(upload_to=None, verbose_name='Archivo')),
            ],
        ),
        migrations.CreateModel(
            name='tr_Alumno_titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('fk_alumtitu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.Alumno_en_titulo')),
                ('fk_idalumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
            ],
        ),
        migrations.AddField(
            model_name='entregatesis',
            name='fk_Tesis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.Tesis'),
        ),
        migrations.AddField(
            model_name='comite',
            name='Director_Tesis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.director_tesis'),
        ),
        migrations.AddField(
            model_name='comite',
            name='Prof_examinador',
            field=models.ManyToManyField(blank=True, to='Titulacion.ProfExaminador', verbose_name=''),
        ),
        migrations.AddField(
            model_name='avancetesis',
            name='fk_entregaTesis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.EntregaTesis'),
        ),
        migrations.AddField(
            model_name='alumno_en_titulo',
            name='avance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.avanceTesis'),
        ),
        migrations.AddField(
            model_name='alumno_en_titulo',
            name='entreegafinal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.EntregaTesisFinal'),
        ),
        migrations.AddField(
            model_name='alumno_en_titulo',
            name='estado_actual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.Estado_Actual'),
        ),
        migrations.AddField(
            model_name='alumno_en_titulo',
            name='estado_anterior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.Estado_Anterior'),
        ),
        migrations.AddField(
            model_name='alumno_en_titulo',
            name='fk_idcomite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.comite'),
        ),
    ]
