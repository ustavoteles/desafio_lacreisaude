# Generated by Django 5.1.6 on 2025-02-10 16:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='data',
        ),
        migrations.AddField(
            model_name='consulta',
            name='data_consulta',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
