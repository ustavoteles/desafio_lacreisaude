# Generated by Django 5.1.6 on 2025-02-10 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0002_rename_profissional_contato_profissional_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='contato',
            field=models.CharField(default='', max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
