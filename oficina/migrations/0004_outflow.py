# Generated by Django 5.0.7 on 2024-07-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0003_alter_service_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Outflow', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]