# Generated by Django 2.2.6 on 2019-12-16 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0024_delete_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100)),
            ],
        ),
    ]
