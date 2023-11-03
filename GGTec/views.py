from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servicio, Empleado
from .forms import EmpleadoForm

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.views import LoginView


#Class based views

class HomeView(TemplateView):
    template_name = 'GGTec/index.html'

class AboutCreate(TemplateView):
    template_name = 'GGTec/aboutme.html'

class EmpresasView(TemplateView):
    template_name = 'GGTec/empresas.html'

class ListaServicios(ListView):
    model = Servicio

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = "Lista de servicios sobre los que encontrarás reseñas."
        return contexto

class ListaEmpleados(ListView):
    model = Empleado

class FiltrarEmpleados(ListView):
    model = Empleado
    template_name = 'ggtec/lista_empleados.html'

    def get_queryset(self):
        servicio_id = self.request.GET.get('servicio')
        empleados = Empleado.objects.all()

        if servicio_id:
            empleados = empleados.filter(servicio_id=servicio_id)
        
        empleados = empleados.order_by('valoracion','costo')
        return empleados

        self.object_list = empleados

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['servicios'] = Servicio.objects.all() 
        return contexto

class EmpleadoCreate(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('Reseñas')

class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('Actualizar_Reseña', args=[self.object.id])+"?ok"

class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('Reseñas')

class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Inicio')
    
    