from django.urls import path
from . import views
from .views import LoginPage, LogoutView
app_name = 'home_app'

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('home/', views.HomePage.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]