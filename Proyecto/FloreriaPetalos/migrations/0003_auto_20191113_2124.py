# Generated by Django 2.2.6 on 2019-11-14 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0002_auto_20191109_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(null=True, upload_to='producto'),
        ),
    ]
