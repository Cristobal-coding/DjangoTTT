from django.urls import path
from django.contrib import admin
from . import views
from .forms import LoginAdmin

admin.autodiscover()
admin.site.login_form = LoginAdmin
app_name = 'home_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]