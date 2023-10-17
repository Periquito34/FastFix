from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from .models import Cliente,Empleado
from .forms import RegistroClienteForm
from django.views import View
from django.contrib.auth.views import LoginView


def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'cliente/login.html')

# View Cliente

class RegistroClienteView(View):
    template_name = 'registro_cliente.html'

    def get(self, request):
        form = RegistroClienteForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leerCliente')  # Reemplaza 'pagina_de_inicio' con la URL a donde deseas redirigir
        return render(request, self.template_name, {'form': form})


class ClienteList(ListView):
    model = Cliente

class ClienteCreate(SuccessMessageMixin, CreateView):
    model= Cliente
    form= Cliente
    fields= '__all__'
    success_message= 'Cliente creado exitosamente'

    def get_success_url(self):
        return reverse('leerCliente')
    
class ClienteUpdate(SuccessMessageMixin, UpdateView):
    model= Cliente
    form= Cliente
    fields= '__all__'
    success_message= 'Cliente actualizado exitosamente'

    def get_success_url(self):
        return reverse('leerCliente')

class ClienteDelete(SuccessMessageMixin, DeleteView):
    model= Cliente
    form= Cliente
    fields= '__all__'
    success_message= 'Cliente eliminado exitosamente'

    def get_success_url(self):
        return reverse('leerCliente')
    
class ClienteDetail(DetailView):
    model= Cliente


# View Empleado

class EmpleadoList(ListView):
    model = Empleado

class EmpleadoCreate(SuccessMessageMixin, CreateView):
    model= Empleado
    form= Empleado
    fields= '__all__'
    success_message= 'Empleado creado exitosamente'

    def get_success_url(self):
        return reverse('leerEmpleado')
    
class EmpleadoUpdate(SuccessMessageMixin, UpdateView):
    model= Empleado
    form= Empleado
    fields= '__all__'
    success_message= 'Empleado actualizado exitosamente'

    def get_success_url(self):
        return reverse('leerEmpleado')
    
class EmpleadoDelete(SuccessMessageMixin, DeleteView):
    model= Empleado
    form= Empleado
    fields= '__all__'
    success_message= 'Empleado eliminado exitosamente'

    def get_success_url(self):
        return reverse('leerEmpleado')
    
class EmpleadoDetail(DetailView):
    model= Empleado

