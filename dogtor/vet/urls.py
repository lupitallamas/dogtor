#1.path
#urpatterns

from django.urls import path

#Views
from .views import Test, OwnersList, OwnerDatail, PetsList, PetDatail, OwnersCreate, OwnersUpdate
from .views import PetsCreate, PetsUpdate


#alias-->(reversed urls) --ª modelos o vista clase
# akuas (reversed urls) --> rutas del proyecto
#si no tienes include --> reversed url se pone como 3er parametro
#si si TIENES INCLUDE --> reverser url se pone como 2do parametro DENTRO  del include () --> include("vet")
urlpatterns =[
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnerDatail.as_view(), name="owners_detail"),
    path("owners/add/", OwnersCreate.as_view(), name="owners_create"),
    path("owners/<int:pk>/edit/", OwnersUpdate.as_view(), name="owners_edit"),
    path("pets/",PetsList.as_view(), name="pets_list"),
    path("pets/<int:pk>/", PetDatail.as_view(), name="pets_detail"),
    path("pets/add/", PetsCreate.as_view(), name="pets_create"),
    path("pets/<int:pk>/edit/", PetsUpdate.as_view(), name="pets_edit"),   
    #path("owners/", list_pet_owners),
    path("test/", Test.as_view())
    
]