# Generated by Django 5.0.7 on 2024-07-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0005_rename_outflow_outflow_outflow'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='pago',
            field=models.BooleanField(default=False),
        ),
    ]
