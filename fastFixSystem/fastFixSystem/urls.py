"""
URL configuration for fastFixSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from fastFix_app.views import ClienteList, ClienteCreate, ClienteDetail, ClienteUpdate, ClienteDelete, EmpleadoList, EmpleadoCreate, EmpleadoDetail, EmpleadoUpdate, EmpleadoDelete, RegistroClienteView
import fastFix_app.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='mainPage'),
    path('login/', views.login, name='login'),

    #URLS de Cliente

    path('leerCliente/', ClienteList.as_view(template_name = "cliente/index.html"), name='leerCliente'),
    path('crearCliente/', ClienteCreate.as_view(template_name = "cliente/crear.html"), name='crearCliente'),
    path('detalleCliente/<int:pk>/', ClienteDetail.as_view(template_name = "cliente/detalle.html"), name='detalleCliente'),
    path('actualizarCliente/<int:pk>/', ClienteUpdate.as_view(template_name = "cliente/actualizar.html"), name='actualizarCliente'),
    path('eliminarCliente/<int:pk>/', ClienteDelete.as_view(template_name = "cliente/eliminar.html"), name='eliminarCliente'),
    path('registroCliente/',RegistroClienteView.as_view(template_name= "cliente/registro.html"), name='registroCliente'),
    

    #URSL de Empleado

    path('leerEmpleado/', EmpleadoList.as_view(template_name = "empleado/index.html"), name='leerEmpleado'),
    path('crearEmpleado/', EmpleadoCreate.as_view(template_name = "empleado/crear.html"), name='crearEmpleado'),
    path('detalleEmpleado/<int:pk>/', EmpleadoDetail.as_view(template_name = "empleado/detalle.html"), name='detalleEmpleado'),
    path('actualizarEmpleado/<int:pk>/', EmpleadoUpdate.as_view(template_name = "empleado/actualizar.html"), name='actualizarEmpleado'),
    path('eliminarEmpleado/<int:pk>/', EmpleadoDelete.as_view(template_name = "empleado/eliminar.html"), name='eliminarEmpleado'),
    
]
