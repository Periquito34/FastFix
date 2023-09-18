
from django.shortcuts import render
from .models import Cliente, CategoriaServicio, Solicitud, Empleado
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

def index(request):
    return render(request, 'index.html')

#CategoriaServicio

class CategoriaServicio(ListView):
    model = CategoriaServicio

class CategoriaServicioCrear(SuccessMessageMixin, CreateView):
    model= CategoriaServicio
    form= CategoriaServicio
    fields= '__all__'
    success_message= 'Categoria de Servicio creada exitosamente'

    def get_success_url(self):
        return reverse('leer')

class CategoriaServicioActualizar(SuccessMessageMixin, UpdateView):
    model= CategoriaServicio
    form= CategoriaServicio
    fields= '__all__'
    success_message= 'Categoria de Servicio actualizada exitosamente'

    def get_success_url(self):
        return reverse('leer')

class CategoriaServicioEliminar(SuccessMessageMixin, DeleteView):
    model= CategoriaServicio
    form= CategoriaServicio
    fields= '__all__'
    success_message= 'Categoria de Servicio eliminada exitosamente'

    def get_success_url(self):
        return reverse('leer')

class CategoriaServicioDetail(DetailView):
    model= CategoriaServicio


#Empleado

class Empleado(ListView):
    model = Empleado

class EmpleadoCrear(SuccessMessageMixin, CreateView):
    model= Empleado
    form= Empleado
    fields= '__all__'
    success_message= 'Empleado creado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class EmpleadoActualizar(SuccessMessageMixin, UpdateView):
    model= Empleado
    form= Empleado
    fields= '__all__'
    success_message= 'Empleado actualizado exitosamente'
    
    def get_success_url(self):
        return reverse('leer')
    
    
class EmpleadoEliminar(SuccessMessageMixin, DeleteView):
    model= Empleado
    form= Empleado
    fields= '__all__'
    success_message= 'Empleado eliminado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class EmpleadoDetail(DetailView):
    model= Empleado
    

#Cliente
    
    
class ClienteDelete(SuccessMessageMixin, DeleteView):
    model = Cliente
    form = Cliente
    fields = '__all__'
    success_message = 'Cliente eliminado correctamente'

    def get_success_url(self):
        return reverse('leer')

class ClienteList(ListView):
    model = Cliente

class ClienteCreate(SuccessMessageMixin, CreateView):
    model = Cliente
    form = Cliente
    fields = '__all__'
    success_message = 'Cliente creado correctamente'

    def get_success_url(self):
        return reverse('leer')
    
class ClienteDetail(DetailView):
    model = Cliente

class ClienteUpdate(SuccessMessageMixin, UpdateView):
    model = Cliente
    form = Cliente
    fields = '__all__'
    success_message = 'Cliente actualizado correctamente'

    def get_success_url(self):
        return reverse('leer')


