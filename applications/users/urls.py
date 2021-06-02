from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('usuarios/', views.UserMainView.as_view(), name='registrar'),
    path('usuarios/lock/<pk>', views.lock, name='bloquear'),
    path('usuarios/unlock/<pk>', views.unlock, name='desbloquear'),
]