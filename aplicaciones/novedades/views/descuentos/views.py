from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from xhtml2pdf import pisa

from aplicaciones.novedades.forms import PrestamoForm, DescuentoForm
from aplicaciones.novedades.models import FacturaPrestamo, Descuentos
from aplicaciones.novedades.utils import generar_pdf


class lisDescuentos(ListView):
    template_name = 'descuentos/lisdescuentos.html'
    context_object_name = 'lisdescuentos'
    model = Descuentos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/novedades/menunovedades'
        context['listar_url'] = ''
        context['crear_url'] = '/novedades/creardescuentos'
        context['imprimir_url'] = '/novedades/pdf_descuentos'
        context['titulo'] = 'LISTADO DE DESCUENTOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class ListaDescuentosPDF(View):
    def get(self,request,*args,**kwargs):
        lisdescuentos=Descuentos.objects.all()
        data={
            'lisdescuentos':lisdescuentos
        }
        pdf = generar_pdf('descuentos/pdfdescuentos.html',data)
        return HttpResponse(pdf, content_type='application/pdf')

class CrearDescuentos(CreateView):
    template_name = 'descuentos/creardescuestos.html'
    model = Descuentos
    success_url = reverse_lazy('novedades:lisdescuentos')
    form_class = DescuentoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/novedades/creardescuentos'
        context['titulo'] = 'CREAR DESCUENTO'
        context['url_anterior'] = '/novedades/lisdescuentos'
        context['listar_url'] = '/novedades/lisdescuentos'
        context['action'] = 'add'
        return context

class ActualizarDescuento(UpdateView):
    model = Descuentos
    template_name = "descuentos/creardescuestos.html"
    success_url = reverse_lazy('novedades:lisdescuentos')
    form_class = DescuentoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DESCUENTO'
        context['url_anterior'] = '/novedades/lisdescuentos'
        context['listar_url'] = '/novedades/lisdescuentos'
        return context

class EliminarDescuento(DeleteView):
    model = Descuentos
    template_name = "descuentos/deletedescuentos.html"
    success_url = reverse_lazy('novedades:lisdescuentos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE DESCUENTO'
        context['url_anterior'] = '/novedades/lisdescuentos'
        context['listar_url'] = '/novedades/lisdescuentos'
        return context

class DescuentoPDF(View):
    def get(self,request,*args,**kwargs):
        template= get_template('descuentos/descuentofacpdf.html')
        context = {'descuento': Descuentos.objects.get(pk=self.kwargs['pk'])}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        return response
