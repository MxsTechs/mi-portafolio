from django.db import models

# Create your models here.


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, verbose_name="nombre_usuario")
    contrasenia = models.CharField(
        default="", max_length=30, verbose_name="contrasenia_usuario"
    )
    correo = models.EmailField(
        default="ejemplo@ejemplo.com", verbose_name="correo_usuario"
    )
    direccion = models.CharField(
        max_length=50, default="Santiago, Chile", verbose_name="direccion_usuario"
    )
    numero = models.BigIntegerField(verbose_name="numero_usuario", default="123456789")


class Inventario(models.Model):
    id_prod = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=30, verbose_name="producto")
    cant_producto = models.IntegerField(verbose_name="cant_producto")
    descripcion = models.CharField(
        max_length=200, verbose_name="descripcion", default="Producto X"
    )
    imagen = models.ImageField(upload_to="productos/", verbose_name="imagen", null=True)


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre_Admin = models.CharField(max_length=30, verbose_name="nombre_admin")
    correo_Admin = models.EmailField(
        default="ejemplo@ejemplo.com", verbose_name="correo_admin"
    )
    contrasenia_admin = models.CharField(
        default="", max_length=50, verbose_name="contrasenia_admin"
    )


class Buzon(models.Model):
    id_buzon = models.AutoField(primary_key=True)
    run = models.CharField(max_length=30, verbose_name="run")
    apellido_paterno = models.CharField(max_length=30, verbose_name="apellido_paterno")
    apellido_materno = models.CharField(max_length=30, verbose_name="apellido_materno")
    telefono = models.IntegerField(verbose_name="telefono")
    nombre_solicitud = models.CharField(max_length=30, verbose_name="nombre_solicitud")
    correo_solicitud = models.EmailField(
        default="ejemplo@ejemplo.com", verbose_name="correo"
    )
    mensaje = models.CharField(max_length=300, verbose_name="mensaje")
