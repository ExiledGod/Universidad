# Generated by Django 2.1.2 on 2019-04-29 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Direccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionProfesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=300, null=True)),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Comuna')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
                'ordering': ('region', 'provincia', 'comuna'),
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_pat', models.CharField(max_length=50)),
                ('apellido_mat', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=13)),
                ('fecha_nac', models.DateField()),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=20)),
                ('telefono', models.CharField(max_length=12, null=True)),
                ('mail', models.EmailField(blank=True, max_length=300, null=True)),
                ('profesion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'ordering': ('nombre', 'apellido_pat'),
            },
        ),
        migrations.CreateModel(
            name='Tipo_grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(choices=[('Licenciatura', 'Licenciatura'), ('Titulo Profesional', 'Titulo Profesional'), ('Magister', 'Magister'), ('Doctorado', 'Doctorado')], max_length=30)),
                ('institucion', models.CharField(max_length=100, null=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('anio_obtencion', models.CharField(max_length=4, null=True)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profesor.Profesor')),
            ],
            options={
                'verbose_name': 'Grado',
                'verbose_name_plural': 'Grados',
                'ordering': ('profesor', 'nombre_tipo'),
            },
        ),
        migrations.AddField(
            model_name='direccionprofesor',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profesor.Profesor'),
        ),
        migrations.AddField(
            model_name='direccionprofesor',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Provincia'),
        ),
        migrations.AddField(
            model_name='direccionprofesor',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Region'),
        ),
    ]
