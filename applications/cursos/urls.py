from django.urls import path
from . import views
app_name = 'cursos_app'

urlpatterns = [
    path('cursos/', views.CursosHome.as_view(), name='all'),
    path('cursos/view/<pk>/', views.CursosDetalle.as_view(), name='detalleCurso'),
    path('cursos/finish/semestre/', views.finalizar_año, name='finishA'),
    path('cursos/gestion/alumnos/', views.gestionar_alumnos, name='gestionar'),
    path('cursos/mover/alumno/', views.remove_alumno, name='removerAlum'),
    path('cursos/init/', views.init_cursos, name='initCursos'),
]