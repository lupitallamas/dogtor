from django.shortcuts import render
from rest_framework import viewsets,generics
from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializers, PetsSerializers, PetdateSerializer, OwnersListSerializer
from .serializers import OwnersDetailSerializer
# Create your views here.
# class OwnersViewSet(viewsets.ModelViewSet):
#     """ViewSet del Modelo PetOwner."""
#     #1, query que se va a realizar querys con el shell 
#     #2. El serializador sontrolan como se van a ver nuestros datos
    
#     #Obtener todos los owners --> PetOwners.objects.all()
#     queryset = PetOwner.objects.all()
#     serializer_class = OwnersSerializers
    
# class PetviewSet(viewsets.ModelViewSet):
#     """ViewSet del Modelo Pet."""
      
#     queryset = Pet.objects.all()
#     serializer_class = PetsSerializers   
    
# class PetDateviewSet(viewsets.ModelViewSet):
#     """ViewSet del Model PetDate."""     
#     queryset = PetDate.objects.all()
#     serializer_class = PetdateSerializer

class ListOwnersAPIView(generics.ListAPIView):
    """List Owners Api View"""
    queryset = PetOwner.objects.all().order_by("created_at")
    #seializer
    serializer_class = OwnersListSerializer
    
class RetriveOwnersAPIView(generics.RetrieveAPIView):
    """Solo ver id, first_name , last_name de un owner"""
    queryset=PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer
    
class CreateOwnersAPIView(generics.CreateAPIView):
    """Crear un Owner con la Api"""
    queryset=PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer
    
class UpdateOwnersAPIView(generics.UpdateAPIView):
    """Update de Owner"""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers

class DeleteOwnersAPIView(generics.DestroyAPIView):
    """Borrar un owner"""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer
    
class RetriveUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Update,delete,get de PetOwners"""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers

class ListCreateOwnerAPIView(generics.ListCreateAPIView):
    """list y Create de Pet Owners"""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers

    
    
    