# Generated by Django 2.2.6 on 2019-12-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0015_auto_20191207_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
        migrations.AddField(
            model_name='estado',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estado',
            name='nombre_estado',
            field=models.CharField(max_length=45),
        ),
    ]
