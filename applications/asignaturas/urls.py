from django.urls import path
from . import views
app_name = 'asignaturas_app'

urlpatterns = [
    path('asignaturas/', views.AsignaturasView.as_view(), name='overview'),
    path('planes_de_estudio/', views.PlanesView.as_view(), name='planes'),
    
]