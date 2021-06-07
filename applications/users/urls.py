from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('usuarios/', views.UserMainView.as_view(), name='registrar'),
    path('usuarios/register/user', views.CreateUser.as_view(), name='usercreate'),
    path('usuarios/register/rol', views.CreateRol.as_view(), name='rolcreate'),
]