# Generated by Django 5.1 on 2024-11-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
