# Generated by Django 2.2.6 on 2019-11-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0006_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
