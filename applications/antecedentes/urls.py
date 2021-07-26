from django.urls import path
from . import views
# from .views import AlumnosHome, AlumnosFiltros
app_name = 'antecedentes_app'

urlpatterns = [
    path('antecedentes/', views.AntecedentesView.as_view(), name='inicio'),
    path('antecedentes/create/', views.antecedente_create, name='create'),
    path('antecedentes/edit/<pk>', views.edit_antecedente, name='edit'),
]