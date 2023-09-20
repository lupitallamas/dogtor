from django.shortcuts import render
from rest_framework import viewsets
from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializers, PetsSerializers, PetdateSerializer

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """ViewSet del Modelo PetOwner."""
    #1, query que se va a realizar querys con el shell 
    #2. El serializador sontrolan como se van a ver nuestros datos
    
    #Obtener todos los owners --> PetOwners.objects.all()
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers
    
class PetviewSet(viewsets.ModelViewSet):
    """ViewSet del Modelo Pet."""
    queryset = Pet.objects.all()
    serializer_class = PetsSerializers   
    
class PetDateviewSet(viewsets.ModelViewSet):
    """ViewSet del Model PetDate."""     
    queryset = PetDate.objects.all()
    serializer_class = PetdateSerializer
    
    
    