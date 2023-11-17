from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('activos/', views.activo_list),
    path('activocreate/', csrf_exempt(views.activo_create), name='activoCreate'),
]