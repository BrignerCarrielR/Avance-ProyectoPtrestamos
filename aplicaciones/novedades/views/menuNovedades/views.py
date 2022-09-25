from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class NovedadesTemplateView(TemplateView):
    template_name = 'novedades.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Novedades"
        context['url_anterior'] = "/"
        return context