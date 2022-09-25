from django.shortcuts import HttpResponse
import json
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from aplicaciones.novedades.forms import PrestamoForm
from aplicaciones.novedades.models import FacturaPrestamo


class lisPrestamos(ListView):
    template_name = 'prestamos/lisprestamos.html'
    context_object_name = 'lisprestamos'
    model = FacturaPrestamo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/novedades/menunovedades'
        context['listar_url'] = ''
        context['crear_url'] = '/novedades/crearprestamos'
        context['titulo'] = 'LISTADO DE PRESTAMOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearPrestamo(CreateView):
    template_name = 'prestamos/crearprestamos.html'
    model = FacturaPrestamo
    success_url = reverse_lazy('novedades:lisprestamos')
    form_class = PrestamoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/novedades/crearprestamos'
        context['titulo'] = 'CREAR PRESTAMO'
        context['url_anterior'] = '/novedades/lisprestamos'
        context['listar_url'] = '/novedades/lisprestamos'
        context['action'] = 'add'
        return context

class ActualizarPrestamo(UpdateView):
    model = FacturaPrestamo
    template_name = "prestamos/crearprestamos.html"
    success_url = reverse_lazy('novedades:lisprestamos')
    form_class = PrestamoForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR PRESTAMO'
        context['listar_url'] = '/novedades/lisprestamos'
        return context

class EliminarPrestamo(DeleteView):
    model = FacturaPrestamo
    template_name = "prestamos/deleteprestamos.html"
    success_url = reverse_lazy('novedades:lisprestamos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE PRESTAMO'
        context['listar_url'] = '/novedades/lisprestamos'
        return context