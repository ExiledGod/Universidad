# Generated by Django 2.1.2 on 2019-05-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0003_cobros'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='beca',
            field=models.BooleanField(default=False),
        ),
    ]