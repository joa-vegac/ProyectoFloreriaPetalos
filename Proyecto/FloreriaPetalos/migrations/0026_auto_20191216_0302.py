# Generated by Django 2.2.6 on 2019-12-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0025_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='nombre_estado',
            field=models.CharField(max_length=100),
        ),
    ]
