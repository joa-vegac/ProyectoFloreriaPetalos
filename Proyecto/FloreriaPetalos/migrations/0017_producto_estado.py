# Generated by Django 2.2.6 on 2019-12-08 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FloreriaPetalos', '0016_auto_20191208_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FloreriaPetalos.Estado'),
            preserve_default=False,
        ),
    ]
