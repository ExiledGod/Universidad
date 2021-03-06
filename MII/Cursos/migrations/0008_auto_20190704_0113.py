# Generated by Django 2.1.2 on 2019-07-04 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0007_auto_20190704_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='trimestral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='nivelacion1',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='nivelacion2',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='avancecurricular',
            name='nivelacion1',
        ),
        migrations.RemoveField(
            model_name='avancecurricular',
            name='nivelacion2',
        ),
        migrations.AlterField(
            model_name='cursos',
            name='creditos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='nivelacion1',
        ),
        migrations.DeleteModel(
            name='nivelacion2',
        ),
        migrations.AddField(
            model_name='trimestral',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.Cursos'),
        ),
        migrations.AddField(
            model_name='avancecurricular',
            name='trimestral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.trimestral'),
        ),
    ]
