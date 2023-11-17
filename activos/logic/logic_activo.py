from ..models import Activo

def get_activos():
    queryset = Activo.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_activo(form):
    activo = form.save()
    activo.save()
    return ()