from django.urls import path
from . import views
# from .views import AlumnosHome, AlumnosFiltros
app_name = 'alumnos_app'

urlpatterns = [
    path('alumnos/', views.AlumnosHome.as_view(), name='inicio'),
    path('alumnos/listado/', views.AlumnosFiltros.as_view(), name='filtrar'),
    path('alumnos/listado/edit/<pk>/', views.AlumnoEdit.as_view(), name='actualizar'),
    path('alumnos/registrar/', views.AlumnosRegister.as_view(), name='registrar'),
    path('alumnos/apoderados/', views.ApoderadosList.as_view(), name='apoderados'),
    path('alumnos/apoderados/register/', views.CreateApoderado.as_view(), name='addApoderado'),
    path('alumnos/delete/<pk>', views.delete_alumno, name='eliminar'),
]