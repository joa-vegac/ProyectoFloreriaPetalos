# Generated by Django 2.2.6 on 2019-12-07 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0014_auto_20191203_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
