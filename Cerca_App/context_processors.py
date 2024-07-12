# myapp/context_processors.py

from .models import Usuario
import logging

logger = logging.getLogger(__name__)


def usuario_context(request):
    usuarioVista = None
    if "usuario_id" in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session["usuario_id"])
            usuarioVista = usuario.nombre
        except Usuario.DoesNotExist:
            pass
    logger.debug(f"usuarioVista: {usuarioVista}")
    return {"usuarioVista": usuarioVista}
