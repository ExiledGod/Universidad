# Generated by Django 2.1.2 on 2019-05-11 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malla_curricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malla', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='cursos',
            name='curso_en_malla',
            field=models.CharField(choices=[('Nuevo', 'Nuevo'), ('Antiguo', 'Antiguo')], default='Nuevo', max_length=40),
        ),
        migrations.AddField(
            model_name='malla_curricular',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.Cursos'),
        ),
    ]
