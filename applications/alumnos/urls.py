from django.urls import path
from . import views
# from .views import AlumnosHome, AlumnosFiltros
app_name = 'alumnos_app'

urlpatterns = [
    path('alumnos/', views.AlumnosHome.as_view(), name='inicio'),
    path('alumnos/filtros/', views.AlumnosFiltros.as_view(), name='filtrar'),
    path('alumnos/filtros/edit/<pk>/', views.AlumnoEdit.as_view(), name='actualizar'),
    path('alumnos/registrar/', views.AlumnosRegister.as_view(), name='registrar'),
    # path('alumnos/filtros/delete/<pk>/', views.AlumnoDelete.as_view(), name='eliminar'),
    path('alumnos/delete/<pk>', views.delete_alumno, name='eliminar'),
]