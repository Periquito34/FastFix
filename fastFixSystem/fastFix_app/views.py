
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