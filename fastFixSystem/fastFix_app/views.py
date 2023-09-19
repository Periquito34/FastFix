from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from .models import Solicitud, Cliente, CategoriaServicio, Empleado


# View Cliente

class Cliente(ListView):
    model = Cliente

class ClienteCrear(SuccessMessageMixin, CreateView):
    model= Cliente
    form= Cliente
    fields= '__all__'
    success_message= 'Cliente creado exitosamente'

    def get_success_url(self):
        return reverse('leer')
    
class ClienteActualizar(SuccessMessageMixin, UpdateView):
    model= Cliente
    form= Cliente
    fields= '__all__'
    success_message= 'Cliente actualizado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class ClienteEliminar(SuccessMessageMixin, DeleteView):
    model= Cliente
    form= Cliente
    fields= '__all__'
    success_message= 'Cliente eliminado exitosamente'

    def get_success_url(self):
        return reverse('leer')
    
class ClienteDetail(DetailView):
    model= Cliente


# View CategoriaServicio

class CategoriaServicio(ListView):
    model = CategoriaServicio

class CategoriaServicioCrear(SuccessMessageMixin, CreateView):
    model= CategoriaServicio
    form= CategoriaServicio
    fields= '__all__'
    success_message= 'CategoriaServicio creado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class CategoriaServicioActualizar(SuccessMessageMixin, UpdateView):
    model= CategoriaServicio
    form= CategoriaServicio
    fields= '__all__'
    success_message= 'CategoriaServicio actualizado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class CategoriaServicioEliminar(SuccessMessageMixin, DeleteView):
    model= CategoriaServicio
    form= CategoriaServicio
    fields= '__all__'
    success_message= 'CategoriaServicio eliminado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class CategoriaServicioDetail(DetailView):
    model= CategoriaServicio

# View Empleado

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


# View Solicitud

class Solicitud(ListView):
    model = Solicitud

class SolicitudCrear(SuccessMessageMixin, CreateView):
    model= Solicitud
    form= Solicitud
    fields= '__all__'
    success_message= 'Solicitud creado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class SolicitudActualizar(SuccessMessageMixin, UpdateView):
    model= Solicitud
    form= Solicitud
    fields= '__all__'
    success_message= 'Solicitud actualizado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class SolicitudEliminar(SuccessMessageMixin, DeleteView):
    model= Solicitud
    form= Solicitud
    fields= '__all__'
    success_message= 'Solicitud eliminado exitosamente'

    def get_success_url(self):
        return reverse('leer')

class SolicitudDetail(DetailView):
    model= Solicitud
    




