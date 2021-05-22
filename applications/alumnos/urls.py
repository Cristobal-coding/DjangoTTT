from django.urls import path
from . import views
from .views import AlumnosHome, AlumnosFiltros
app_name = 'alumnos_app'

urlpatterns = [
    path('alumnos/', views.AlumnosHome.as_view(), name='inicio'),
    path('filtros/', views.AlumnosFiltros.as_view(), name='filtrar'),

]