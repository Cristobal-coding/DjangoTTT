from django.urls import path
from . import views
app_name = 'asignaturas_app'

urlpatterns = [
    path('asignaturas/', views.AsignaturasView.as_view(), name='overview'),
    path('planes_de_estudio/', views.PlanesView.as_view(), name='planes'),
    path('asignatura/add/profesor/', views.profe_to_asign, name='addProfe'),
    path('asignatura/generar/data/', views.init_all, name='initGenerador'),
    path('profesores/', views.ProfesoresView.as_view(), name='profesores'),
    path('profesores/create', views.profesor_create, name='createProfesor'),
    path('profesores/edit', views.profesor_edit, name='editProfesor'),
    
]