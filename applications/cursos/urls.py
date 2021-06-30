from django.urls import path
from . import views
app_name = 'cursos_app'

urlpatterns = [
    path('cursos/', views.CursosHome.as_view(), name='All'),
]