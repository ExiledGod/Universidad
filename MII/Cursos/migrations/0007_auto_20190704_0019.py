# Generated by Django 2.1.2 on 2019-07-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0006_auto_20190702_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='tipo',
            field=models.CharField(choices=[('Optativo', 'Optativo'), ('Obligatorio', 'Obligatorio'), ('Nivelacion', 'Nivelacion')], max_length=12),
        ),
    ]
