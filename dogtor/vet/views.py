from django.shortcuts import render

# Create your views  como funcion hay vistas de clasehere.
#Models
from vet.models import PetOwner, Pet
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
#forms

from .forms import OwnerForm, PetForm

def list_pet_owners(request):
    #Agarrar infromacion de base de datos
    owners = PetOwner.objects.all()
   
    #Hacemos el contexto
    context = {"owners": owners }
    #templates
    template = loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context,request))

# PascalCase
# class OwnersList(TemplateView):
#    template_name=  "vet/owners/list.html"
#    def get_context_data(self, **kwargs):
#        #Agarrar el contexto que ya creo 'TemplateView'
#        context = super().get_context_data(**kwargs)
#        #le agregamos nuestro custom context
#        context["owners"] = PetOwner.objects.all()
#        return context


# class PetDatail(TemplateView):
#    template_name=  "vet/pets/Detail.html"
#    def get_context_data(self, **kwargs):
#        #Agarrar el contexto que ya creo 'TemplateView'
#        context = super().get_context_data(**kwargs)
#        #le agregamos nuestro custom context
#        context["pet"] = Pet.objects.get(pk=kwargs["pk"])
#        return context
# class PetsList(TemplateView):
#    template_name=  "vet/pets/list.html"
#    def get_context_data(self, **kwargs):
#        #Agarrar el contexto que ya creo 'TemplateView'
#        context = super().get_context_data(**kwargs)
#        #le agregamos nuestro custom context
#        context["pets"] = Pet.objects.all()
#        return context

class PetsList(ListView):
   #1, Modelo con el que estamos manipulando
    #Templete con el quevamos a renderizar
    # 3. El contexto que va a tener este template
    model = Pet #1
    template_name = "vet/pets/list.html" #2
    context_object_name="pets" #3
   
class PetDatail(DetailView):
   """Render a """
   model = Pet
   template_name= "vet/pets/detail.html"
   context_object_name="pet"
 
class OwnersList(ListView):
    #1, Modelo con el que estamos manipulando
    #Templete con el quevamos a renderizar
    # 3. El contexto que va a tener este template
    model = PetOwner #1
    template_name = "vet/owners/list.html" #2
    context_object_name="owners" #3  
    
class OwnerDatail(DetailView):
    """Render a specific pet"""
    model = PetOwner #1
    template_name = "vet/owners/detail.html" #2
    context_object_name="owner" #3
     
class Test(View):
    #Como funcion el metodo(GET,PATCH,POST,DELETE,PUT)
    def get(self,request):
        return HttpResponse("Hello world from a class generic views")
    
class OwnersCreate(CreateView):
    """View used to create a PetOwner."""
    #1. Modelo
    #2. Template a renderizar
    #3. No es necesario pasarle el contexto porque no pasamos la bd, pero, El formulario con
    #con el que va a crar
    #4. La urls si la request fue exitosa-->reversed_url
    
    model = PetOwner
    template_name="vet/owners/create.html"
    form_class = OwnerForm
    success_url=reverse_lazy("vet:owners_list")

class OwnersUpdate(UpdateView):
    """View used to update a PetOwner"""
    model = PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")
 
 
class PetsCreate(CreateView):
    """View used to create a PetOwner."""
    #1. Modelo
    #2. Template a renderizar
    #3. No es necesario pasarle el contexto porque no pasamos la bd, pero, El formulario con
    #con el que va a crar
    #4. La urls si la request fue exitosa-->reversed_url
    
    model = Pet
    template_name="vet/pets/create.html"
    form_class = PetForm
    success_url=reverse_lazy("vet:pets_list")

class PetsUpdate(UpdateView):
    """View used to update a Pet"""
    model = Pet
    template_name = "vet/pets/update.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pets_list")   