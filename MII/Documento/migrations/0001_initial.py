# Generated by Django 2.1.2 on 2019-04-29 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumno', '0001_initial'),
        ('Profesor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_doc', models.CharField(choices=[('Tesis', 'Tesis'), ('Investigacion', 'Investigacion')], max_length=20)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profesor.Profesor')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'ordering': ('tipo_doc', 'nombre', 'alumno', 'profesor'),
            },
        ),
    ]
