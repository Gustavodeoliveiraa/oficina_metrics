# Generated by Django 5.0.7 on 2024-07-23 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0004_outflow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outflow',
            old_name='Outflow',
            new_name='outflow',
        ),
    ]
