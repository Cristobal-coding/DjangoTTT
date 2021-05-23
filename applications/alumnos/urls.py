from django.urls import path
from . import views
from .views import AlumnosHome, AlumnosFiltros
app_name = 'alumnos_app'

urlpatterns = [
    path('alumnos/', views.AlumnosHome.as_view(), name='inicio'),
    path('alumnos/filtros/', views.AlumnosFiltros.as_view(), name='filtrar'),
    path('alumnos/registrar/', views.AlumnosRegister.as_view(), name='registrar'),

]