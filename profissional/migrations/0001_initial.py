# Generated by Django 5.1.6 on 2025-02-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profissional_nome', models.CharField(default='', max_length=100)),
                ('profissional_nome_social', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('profissional_profissao', models.CharField(default='', max_length=100)),
                ('profissional_contato', models.CharField(default='', max_length=100)),
                ('profissional_endereco', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
