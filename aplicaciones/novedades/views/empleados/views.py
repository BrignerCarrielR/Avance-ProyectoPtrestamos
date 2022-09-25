from django.urls import reverse_lazy

from aplicaciones.novedades.models import Empleado
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aplicaciones.novedades.forms import EmpleadoForm

class ListaEmpleadosListView(ListView):
    template_name = "empleados/lisempleados.html"
    context_object_name = 'lisempleados'
    model = Empleado
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/novedades/menunovedades'
        context['listar_url']= ''
        context['crear_url'] = '/novedades/crearempleado'
        context['titulo'] = 'LISTADO DE EMPLEDOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearEmpleado(CreateView):
    model = Empleado
    template_name = "empleados/crearempleado.html"
    success_url = reverse_lazy('novedades:listaempleados')
    form_class = EmpleadoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'NUEVO EMPLEADO'
        context['url_anterior'] = '/novedades/listaempleados'
        context['listar_url'] = '/novedades/listaempleados'
        # context['action'] = 'add'
        # formulario=context['action']
        # print(formulario)
        return context

class ActualizarEmpleado(UpdateView):
    model = Empleado
    template_name = "empleados/crearempleado.html"
    success_url = reverse_lazy('novedades:listaempleados')
    form_class = EmpleadoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE EMPLEADO'
        context['url_anterior'] = '/novedades/listaempleados'
        context['listar_url'] = '/novedades/listaempleados'
        return context

class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = "empleados/deleteempleado.html"
    success_url = reverse_lazy('novedades:listaempleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE EMPLEADO'
        context['listar_url'] = '/novedades/listaempleados'
        return context