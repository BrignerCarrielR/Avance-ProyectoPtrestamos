from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from aplicaciones.novedades.models import Empresas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aplicaciones.novedades.forms import EmpleadoForm, EmpresaForm
from aplicaciones.novedades.utils import generar_pdf


class ListaEmpresaListView(ListView):
    template_name = "empresa/lisempresa.html"
    context_object_name = 'lisempresa'
    model = Empresas

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombre__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/novedades/menunovedades'
        context['listar_url']= '/novedades/lisempresa'
        context['crear_url'] = '/novedades/crearempresa'
        context['imprimir_url'] = '/novedades/pdf_empresa'
        context['titulo'] = 'LISTADO DE EMPRESAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class ListaempresaPDF(View):
    def get(self,request,*args,**kwargs):
        lisempresa=Empresas.objects.all()
        data={
            'lisempresa':lisempresa
        }
        pdf = generar_pdf('empresa/pdfempresa.html',data)
        return HttpResponse(pdf, content_type='application/pdf')

class CrearEmpresa(CreateView):
    model = Empresas
    template_name = "empresa/crearempresa.html"
    success_url = reverse_lazy('novedades:lisempresa')
    form_class = EmpresaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'NUEVA EMPRESA'
        context['url_anterior'] = '/novedades/lisempresa'
        context['listar_url'] = '/novedades/lisempresa'
        # context['action'] = 'add'
        # formulario=context['action']
        # print(formulario)
        return context

class ActualizarEmpresa(UpdateView):
    model = Empresas
    template_name = "empresa/crearempresa.html"
    success_url = reverse_lazy('novedades:lisempresa')
    form_class = EmpresaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['url_anterior'] = '/novedades/lisempresa'
        context['titulo'] = 'ACTUALIZAR EMPRESA'
        context['listar_url'] = '/novedades/lisempresa'
        return context

class EliminarEmpresa(DeleteView):
    model = Empresas
    template_name = "empresa/deleteempresa.html"
    success_url = reverse_lazy('novedades:lisempresa')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE EMPRESA'
        context['listar_url'] = '/novedades/lisempresa'
        return context