from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('usuarios/', views.UserMainView.as_view(), name='registrar'),
    path('usuarios/register/user', views.CreateUser.as_view(), name='usercreate'),
    path('usuarios/profile/', views.ProfileView.as_view(), name='profile'),
    path('usuarios/profile/edit', views.edit_profile, name='editprofile'),
]