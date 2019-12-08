# Generated by Django 2.2.6 on 2019-12-03 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0009_auto_20191203_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('nombre_estado', models.CharField(default='Disponible', max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='FloreriaPetalos.Estado'),
            preserve_default=False,
        ),
    ]