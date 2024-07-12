from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ADMIN
    path("logmin/", views.logmin, name="logmin"),
    path("CerrarSesion", views.CerrarSesion, name="CerrarSesion"),
    # admin
    path("admin/", views.admin, name="admin"),
    path("admin_buzon/", views.admin_buzon, name="admin_buzon"),
    path("admin_inventario/", views.admin_inventario, name="admin_inventario"),
    path("admin_pedidos/", views.admin_pedidos, name="admin_pedidos"),
    path("admin_permisos/", views.admin_permisos, name="admin_permisos"),
    path("admin_usuarios/", views.admin_usuarios, name="admin_usuarios"),
    # PRINCIPAL
    path("", views.home, name="home"),
    path("carro-vista.html/", views.carro, name="carro"),
    path("jarabes-catalogo.html/", views.jarabes, name="jarabes"),
    path("login-vista.html/", views.login, name="login"),
    path("ofertas-vistas.html/", views.ofertas, name="ofertas"),
    path("pastillas-catalogo.html/", views.pastillas, name="pastillas"),
    path("pedido-vista.html/", views.pedido, name="pedido"),
    path("quienessomos-vista.html/", views.quienessomos, name="quienessomos"),
    path("registro-vista.html/", views.registro, name="registro"),
    path("sexual-catalogo.html/", views.sexual, name="sexual"),
    path("solicitud-vista.html/", views.solicitud, name="solicitud"),
    path("targetaparapago-carro.html/", views.targetaparapago, name="targetaparapago"),
    path(
        "todoslosproductos-catalogo.html/",
        views.todoslosproductos,
        name="todoslosproductos",
    ),
    path(
        "ubicacionusuario-vista.html/", views.ubicacionusuario, name="ubicacionusuario"
    ),
    # METODOS CRUD USUARIO-------------------------------------------------------------------------------------------
    # METODOS CRUD USUARIO-------------------------------------------------------------------------------------------
    # METODOS CRUD USUARIO-------------------------------------------------------------------------------------------
    # METODOS CRUD USUARIO-------------------------------------------------------------------------------------------
    # METODOS CRUD USUARIO-------------------------------------------------------------------------------------------
    path(
        "usuario-admin/agregar-usuario", views.agregar_usuario, name="agregar_usuario"
    ),
    path(
        "usuario-admin/agregar-usuario1",
        views.agregar_usuario1,
        name="agregar_usuario1",
    ),
    path(
        "usuario-admin/ModificarUsuario/<id>",
        views.ModificarUsuario,
        name="ModificarUsuario",
    ),
    path("EliminarUsuario/<id>", views.EliminarUsuario, name="EliminarUsuario"),
    path("Filtrar", views.Filtrar, name="Filtrar"),
    # METODOS CRUD Inventarios---------------------------------------------------------------------------------------
    # METODOS CRUD Inventarios---------------------------------------------------------------------------------------
    # METODOS CRUD Inventarios---------------------------------------------------------------------------------------
    # METODOS CRUD Inventarios---------------------------------------------------------------------------------------
    # METODOS CRUD Inventarios---------------------------------------------------------------------------------------
    path(
        "inventario-admin/agregar-inventario",
        views.agregar_inventario,
        name="agregar_inventario",
    ),
    path(
        "inventario-admin/ModificarInventario/<id_prod>",
        views.ModificarInventario,
        name="ModificarInventario",
    ),
    path(
        "EliminarInventario/<id_prod>",
        views.EliminarInventario,
        name="EliminarInventario",
    ),
    path("FiltrarInventario", views.FiltrarInventario, name="FiltrarInventario"),
    # METODOS CRUD Permisos---------------------------------------------------------------------------------------
    # METODOS CRUD Permisos---------------------------------------------------------------------------------------
    # METODOS CRUD Permisos---------------------------------------------------------------------------------------
    # METODOS CRUD Permisos---------------------------------------------------------------------------------------
    # METODOS CRUD Permisos---------------------------------------------------------------------------------------
    path(
        "permisos-admin/agregar-admin",
        views.agregar_admin,
        name="agregar_admin",
    ),
    path(
        "permisos-admin/ModificarAdmin/<id_admin>",
        views.ModificarAdmin,
        name="ModificarAdmin",
    ),
    path(
        "EliminarAdmin/<id_admin>",
        views.EliminarAdmin,
        name="EliminarAdmin",
    ),
    path(
        "EliminarBuzon/<id_buzon>",
        views.EliminarBuzon,
        name="EliminarBuzon",
    ),
    # CREAR SOLICITUUUUD-------------------------------------------------------------------------------------
    path("crear_solicitud/", views.crear_solicitud, name="crear_solicitud"),
    # --------------------------------------------------------------------------------------------------------
    path("EliminarUsuario/<int:id>/", views.EliminarUsuario, name="EliminarUsuario"),
    # CREAR SOLICITUUUUD-------------------------------------------------------------------------------------
    path("login/", views.login, name="login"),
    path("Cerrar", views.Cerrar, name="Cerrar"),
    path("ajustes/", views.ajustes, name="ajustes"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
