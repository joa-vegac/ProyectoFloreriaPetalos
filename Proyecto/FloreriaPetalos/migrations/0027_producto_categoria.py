# Generated by Django 2.2.6 on 2019-12-16 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0026_auto_20191216_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FloreriaPetalos.Categoria'),
            preserve_default=False,
        ),
    ]