from django.views.generic.base import TemplateView  #Libreria para devolver plantillas html
from django.shortcuts import render

class HomePageView(TemplateView):# Clase que devuelve una plantilla html
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs): #Esta es el método que procesa la respuesta de esta vista y la envia renderizada
        return render(request, self.template_name, {'title':"Web App Gestión de Talento Humano"})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"