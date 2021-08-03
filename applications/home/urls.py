from django.urls import path
from django.contrib import admin
from . import views
app_name = 'home_app'

urlpatterns = [

    path('', views.HomePage.as_view(), name='home'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('lock/user/<pk>/', views.lock_user, name='lockUser'),
    path('unlock/user/<pk>/', views.unlock_user, name='unlockUser'),
]