from django.shortcuts import render
from .models import Cliente, CategoriaServicio, Solicitud, Empleado
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Create your views here.


def index(request):
    return render(request, 'index.html')

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

class ClienteDelete(SuccessMessageMixin, DeleteView):
    model = Cliente
    form = Cliente
    fields = '__all__'
    success_message = 'Cliente eliminado correctamente'

    def get_success_url(self):
        return reverse('leer')
