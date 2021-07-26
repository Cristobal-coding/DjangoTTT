from django.urls import path
from . import views

app_name = 'psicologos_app'

urlpatterns = [

    path('psicologos/', views.InformeView.as_view(), name='inicio'),
    path('psicologos/addinforme/', views.CreateInformeView.as_view(), name='addinforme'),
    # path('psicologos/addinforme/create', views.create, name='create'),
    path('psicologos/informe/<pk>/', views.InformeDetailView.as_view(), name='informe'),
    path('psicologos/informe-pdf/<pk>/', views.InformePDFView.as_view(), name='informe_mostrar'),

    # path('usuarios/', views.UserMainView.as_view(), name='registrar'),
    # path('usuarios/register/user', views.CreateUser.as_view(), name='usercreate'),
    # path('usuarios/register/rol', views.CreateRol.as_view(), name='rolcreate'),
    # path('usuarios/edit/rol/<pk>', views.EditRol.as_view(), name='roledit'),
    # path('usuarios/delete/rol/<pk>', views.DeleteRol, name='roldelete'),
]