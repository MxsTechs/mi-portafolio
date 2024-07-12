# Generated by Django 3.2.8 on 2024-06-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cerca_App', '0003_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Admin', models.CharField(max_length=30, verbose_name='nombre_admin')),
                ('correo_Admin', models.EmailField(default='ejemplo@ejemplo.com', max_length=254, verbose_name='correo_admin')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='contrasenia',
            field=models.CharField(default='', max_length=30, verbose_name='contrasenia_usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default='Santiago, Chile', max_length=50, verbose_name='direccion_usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numero',
            field=models.BigIntegerField(default='123456789', verbose_name='numero_usuario'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cant_producto',
            field=models.IntegerField(verbose_name='cant_producto'),
        ),
    ]
