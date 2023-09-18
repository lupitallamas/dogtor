from django.contrib import admin
from . import models

#from .models import Pet, PetOwner, PetDate

# Register your models here

#Este es el sitio Panel de administracion para la app de 'Vet'
class VetAdminArea(admin.AdminSite):
    """Vet admin panel administracion"""
    site_header = "Vet Site Admin Area"
    
vet_admin_site =VetAdminArea(name="VetAdmin")

#Registramos modelos de Vet en nuestro admin area
vet_admin_site.register(models.PetOwner)
admin.site.register(models.PetOwner)

vet_admin_site.register(models.Pet)
admin.site.register(models.Pet)

vet_admin_site.register(models.PetDate)
admin.site.register(models.PetDate)
