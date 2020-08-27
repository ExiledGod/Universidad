# Generated by Django 2.1.2 on 2019-07-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0008_auto_20190704_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avancecurricular',
            name='semestre1',
        ),
        migrations.AddField(
            model_name='avancecurricular',
            name='semestre1',
            field=models.ManyToManyField(blank=True, to='Cursos.semestre1'),
        ),
        migrations.RemoveField(
            model_name='avancecurricular',
            name='semestre2',
        ),
        migrations.AddField(
            model_name='avancecurricular',
            name='semestre2',
            field=models.ManyToManyField(blank=True, to='Cursos.semestre2'),
        ),
        migrations.RemoveField(
            model_name='avancecurricular',
            name='semestre3',
        ),
        migrations.AddField(
            model_name='avancecurricular',
            name='semestre3',
            field=models.ManyToManyField(blank=True, to='Cursos.semestre3'),
        ),
        migrations.RemoveField(
            model_name='avancecurricular',
            name='trimestral',
        ),
        migrations.AddField(
            model_name='avancecurricular',
            name='trimestral',
            field=models.ManyToManyField(blank=True, to='Cursos.trimestral'),
        ),
    ]
