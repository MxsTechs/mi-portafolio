from django.shortcuts import render, redirect
from .models import Usuario
from .models import Inventario
from .models import Admin
from .models import Buzon


# Create your views here.


# VISTAS DE LA PAGINA EN GENERAL
def carro(request):
    return render(request, "carro-vista.html")


def jarabes(request):
    return render(request, "jarabes-catalogo.html")


def login(request):
    return render(request, "login-vista.html")


def ofertas(request):
    return render(request, "ofertas-vistas.html")


def pastillas(request):
    return render(request, "pastillas-catalogo.html")


def pedido(request):
    return render(request, "pedido-vista.html")


def home(request):
    return render(request, "principal-vista.html")


def quienessomos(request):
    return render(request, "quienessomos-vista.html")


def registro(request):
    return render(request, "registro-vista.html")


def sexual(request):
    return render(request, "sexual-catalogo.html")


def solicitud(request):
    return render(request, "solicitud-vista.html")


def targetaparapago(request):
    return render(request, "targetaparapago-carro.html")


def todoslosproductos(request):
    return render(request, "todoslosproductos-catalogo.html")


def ubicacionusuario(request):
    return render(request, "ubicacionusuario-vista.html")


# CIERRE VISTAS DE LA PAGINA EN GENERAL


# -----------------------------------------------------------------------------------------------------------------------------#
def logmin(request):
    if "admin" in request.session:
        adminVista = request.session["admin"]
        return render(request, "principal-admin.html", {"adminVista": adminVista})
    else:
        if request.POST:
            if Admin.objects.filter(
                correo_Admin=request.POST["correo_Admin"],
                contrasenia_admin=request.POST["contrasenia_admin"],
            ).exists():
                admin = Admin.objects.get(
                    correo_Admin=request.POST["correo_Admin"],
                    contrasenia_admin=request.POST["contrasenia_admin"],
                )
                request.session["admin"] = admin.correo_Admin
                adminVista = request.session["admin"]
                return render(
                    request, "principal-admin.html", {"adminVista": adminVista}
                )
            else:
                return render(request, "logmin/logmin.html")
        else:
            return render(request, "logmin/logmin.html")


def CerrarSesion(request):
    del request.session["admin"]
    admins = Admin.objects.all()
    return render(request, "principal-vista.html", {"admins": admins})


# VISTAS DE LA PAGINA MODO ADMIN


def admin(request):
    usuarios = Usuario.objects.all()
    return render(request, "principal-admin.html", {"usuarios": usuarios})


def admin_buzon(request):
    buzones = Buzon.objects.all()
    return render(request, "buzon-admin.html", {"buzones": buzones})


def admin_inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, "inventario-admin.html", {"inventarios": inventarios})


def admin_pedidos(request):
    return render(request, "pedidos-admin.html")


def admin_permisos(request):
    admins = Admin.objects.all()
    return render(request, "permisos-admin.html", {"admins": admins})


def admin_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuario-admin.html", {"usuarios": usuarios})


# CIERRE VISTAS DE LA PAGINA MODO ADMIN


# CRUD USUARIOS------------------------------------------------------------------------------------------------------------
def agregar_usuario(request):
    if request.method == "POST":
        # insert into gato values()
        usuario = Usuario.objects.create(
            nombre=request.POST["nombre_usuario"],
            correo=request.POST["correoUsuario"],
            contrasenia=request.POST["contrasenia_usuario"],
            direccion=request.POST["direccion_usuario"],
            numero=request.POST["numero_usuario"],
        )
        usuario.save()
        usuarios = Usuario.objects.all()
        return render(request, "usuario-admin.html", {"usuarios": usuarios})
    else:
        return render(request, "agregar/agregar-usuario.html")


def agregar_usuario1(request):
    if request.method == "POST":
        # insert into gato values()
        usuario = Usuario.objects.create(
            nombre=request.POST["nombre_usuario"],
            correo=request.POST["correoUsuario"],
            contrasenia=request.POST["contrasenia_usuario"],
            direccion=request.POST["direccion_usuario"],
            numero=request.POST["numero_usuario"],
        )
        usuario.save()
        usuarios = Usuario.objects.all()
        return render(request, "principal-vista.html", {"usuarios": usuarios})
    else:
        return render(request, "agregar/agregar-usuario.html")


def ModificarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == "POST":
        usuario.correo = request.POST["correoUsuario"]
        usuario.nombre = request.POST["nombre_usuario"]
        usuario.contrasenia = request.POST["contrasenia_usuario"]
        usuario.direccion = request.POST["direccion_usuario"]
        usuario.numero = request.POST["numero_usuario"]
        usuario.save()
        usuarios = Usuario.objects.all()
        return render(request, "usuario-admin.html", {"usuarios": usuarios})
    return render(request, "modificar/ModificarUsuario.html", {"usuario": usuario})


def EliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(to="admin_usuarios")


def Filtrar(request):
    usuarios = Usuario.objects.filter(nombre=request.POST["nombre"])
    return render(request, "usuario-admin.html", {"usuarios": usuarios})


# CRUD INVENTARIO -------------------------------------------------------------------------------------------------------------
def agregar_inventario(request):
    if request.method == "POST":
        # insert into gato values()
        inventario = Inventario.objects.create(
            producto=request.POST["producto"],
            cant_producto=request.POST["cant_producto"],
            descripcion=request.POST["descripcion"],
            imagen=request.FILES["imagen"],
        )
        inventario.save()
        inventarios = Inventario.objects.all()
        return render(request, "inventario-admin.html", {"inventarios": inventarios})
    else:
        return render(request, "agregar/agregar-inventario.html")


def ModificarInventario(request, id_prod):
    inventario = Inventario.objects.get(id_prod=id_prod)
    if request.method == "POST":
        inventario.cant_producto = request.POST["cant_producto"]
        inventario.producto = request.POST["producto"]
        inventario.descripcion = request.POST["descripcion"]
        if "imagen" in request.FILES:
            inventario.imagen = request.FILES["imagen"]
        inventario.save()
        inventarios = Inventario.objects.all()
        return render(request, "inventario-admin.html", {"inventarios": inventarios})
    return render(
        request, "modificar/ModificarInventario.html", {"inventario": inventario}
    )


def EliminarInventario(request, id_prod):
    inventario = Inventario.objects.get(id_prod=id_prod)
    inventario.delete()
    return redirect(to="admin_inventario")


def FiltrarInventario(request):
    inventarios = Inventario.objects.filter(producto=request.POST["producto"])
    return render(request, "inventario-admin.html", {"inventarios": inventarios})


# CRUD ADMIN -------------------------------------------------------------------------------------------------------------
def agregar_admin(request):
    if request.method == "POST":
        admin = Admin.objects.create(
            nombre_Admin=request.POST["nombre_Admin"],
            correo_Admin=request.POST["correo_Admin"],
        )
        admin.save()
        admins = Admin.objects.all()
        return render(request, "permisos-admin.html", {"admins": admins})
    else:
        return render(request, "agregar/agregar-admin.html")


def ModificarAdmin(request, id_admin):
    admin = Admin.objects.get(id_admin=id_admin)
    if request.method == "POST":
        admin.correo_Admin = request.POST["correo_Admin"]
        admin.nombre_Admin = request.POST["nombre_Admin"]
        admin.save()
        admins = Admin.objects.all()
        return render(request, "permisos-admin.html", {"admins": admins})
    return render(request, "modificar/ModificarAdmin.html", {"admin": admin})


def EliminarAdmin(request, id_admin):
    admin = Admin.objects.get(id_admin=id_admin)
    admin.delete()
    return redirect(to="admin_permisos")


# CREAR SOLICITUUUUUD-------------------------------------------------------


def crear_solicitud(request):
    if request.method == "POST":
        # insert into gato values()
        buzon = Buzon.objects.create(
            run=request.POST["run"],
            apellido_paterno=request.POST["apellido_paterno"],
            apellido_materno=request.POST["apellido_materno"],
            telefono=request.POST["telefono"],
            nombre_solicitud=request.POST["nombre_solicitud"],
            correo_solicitud=request.POST["correo_solicitud"],
            mensaje=request.POST["mensaje"],
        )
        buzon.save()
        buzones = Buzon.objects.all()
        return render(request, "solicitud-vista.html", {"buzones": buzones})
    else:
        return render(request, "crear_solicitud/")


def EliminarBuzon(request, id_buzon):
    buzon = Buzon.objects.get(id_buzon=id_buzon)
    buzon.delete()
    return redirect(to="admin_buzon")


# CREAR LOGIIIIIIIIN-------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Usuario


def login(request):
    if "usuario_id" in request.session:
        usuario = Usuario.objects.get(id=request.session["usuario_id"])
        usuarioVista = usuario.nombre  # o cualquier atributo que quieras mostrar
        return render(request, "principal-vista.html", {"usuarioVista": usuarioVista})
    else:
        if request.POST:
            if Usuario.objects.filter(
                correo=request.POST["correo"],
                contrasenia=request.POST["contrasenia"],
            ).exists():
                usuario = Usuario.objects.get(
                    correo=request.POST["correo"],
                    contrasenia=request.POST["contrasenia"],
                )
                request.session["usuario_id"] = usuario.id
                usuarioVista = (
                    usuario.nombre
                )  # o cualquier atributo que quieras mostrar
                return render(
                    request, "principal-vista.html", {"usuarioVista": usuarioVista}
                )
            else:
                return render(request, "login-vista.html")
        else:
            return render(request, "login-vista.html")


def ajustes(request):
    return render(request, "usuario/ajustes-usuario.html")


def Cerrar(request):
    if "usuario_id" in request.session:
        del request.session["usuario_id"]
    return redirect("home")  # Usar redirect en lugar de render
