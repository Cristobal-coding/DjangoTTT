from django.urls import path
from . import views
from .views import AlumnosHome
app_name = 'alumnos_app'

urlpatterns = [
    path('alumnos/', views.AlumnosHome.as_view(), name='inicio'),

]