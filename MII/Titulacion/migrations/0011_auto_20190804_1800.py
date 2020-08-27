# Generated by Django 2.1.2 on 2019-08-04 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profesor', '0002_auto_20190429_1452'),
        ('Titulacion', '0010_auto_20190804_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='inscripcion_tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tema', models.CharField(blank=True, max_length=200, null=True)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.Alumno_en_Titulacion')),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profesor.Profesor')),
            ],
        ),
        migrations.AlterField(
            model_name='detalle',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Titulacion.estado'),
        ),
    ]