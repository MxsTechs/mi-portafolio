# Generated by Django 3.2.8 on 2024-06-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cerca_App', '0002_auto_20240607_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=30, verbose_name='producto')),
                ('cant_producto', models.CharField(max_length=30, verbose_name='cant_producto')),
            ],
        ),
    ]
