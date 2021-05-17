from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('register_user/', views.UserRegisterView.as_view(), name='registrar'),
]