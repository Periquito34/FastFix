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
from fastFix_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cliente/', views.ClienteList.as_view(template_name = "cliente/index.html"), name='leer'),

    path('cliente/crear/', views.ClienteCreate.as_view(template_name = "cliente/crear.html"), name='crear'),

    path('cliente/detalle/<int:pk>/', views.ClienteDetail.as_view(template_name = "cliente/detalle.html"), name='detalle'),

    path('cliente/actualizar/<int:pk>/', views.ClienteUpdate.as_view(template_name = "cliente/actualizar.html"), name='actualizar'),

]
