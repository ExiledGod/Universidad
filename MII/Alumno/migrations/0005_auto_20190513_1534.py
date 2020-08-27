# Generated by Django 2.1.2 on 2019-05-13 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0004_alumno_beca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('anio', models.CharField(max_length=4)),
                ('modalidad', models.CharField(blank=True, choices=[('Semestral', 'Semestral'), ('Trimestre', 'Trimestre')], max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
            ],
        ),
        migrations.AddField(
            model_name='cobros',
            name='derecho_inscripcion',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='cobros',
            name='mensualidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]