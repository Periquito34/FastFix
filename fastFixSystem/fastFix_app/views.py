
#Solcitud


class Solicitud(ListView):
    model = Solicitud

class SolicitudCrear(SuccessMessageMixin, CreateView):
    model= Solicitud
    form= Solicitud
    fields= '__all__'
    success_message= 'Solicitud creada exitosamente'

    def get_success_url(self):
        return reverse('leer')
    
class SolicitudActualizar(SuccessMessageMixin, UpdateView):
    model= Solicitud
    form= Solicitud
    fields= '__all__'
    success_message= 'Solicitud actualizada exitosamente'

    def get_success_url(self):
        return reverse('leer')
    
class SolicitudEliminar(SuccessMessageMixin, DeleteView):
    model= Solicitud
    form= Solicitud
    fields= '__all__'
    success_message= 'Solicitud eliminada exitosamente'

    def get_success_url(self):
        return reverse('leer')
    
class SolicitudDetail(DetailView):
    model= Solicitud

