# Generated by Django 5.1.6 on 2025-02-11 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_alter_consulta_table'),
        ('profissional', '0004_alter_profissional_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='profissional.profissional'),
        ),
    ]
