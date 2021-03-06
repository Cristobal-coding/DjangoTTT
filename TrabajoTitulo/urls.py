"""TrabajoTitulo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path,re_path, include
from django.conf import settings
from django.conf.urls.static import static 
# from applications.home import views
from applications.home.forms import LoginAdmin
admin.autodiscover()
admin.site.login_form=LoginAdmin
# admin.site.login_template='home/login_admin.html'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/login', views.LoginPage.as_view()),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.alumnos.urls')),
    re_path('', include('applications.cursos.urls')),
    re_path('', include('applications.psicologos.urls')),
    re_path('', include('applications.antecedentes.urls')),
    re_path('', include('applications.asignaturas.urls')),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
