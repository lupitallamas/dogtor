from django.urls import path, include

from rest_framework import routers

#Views
from .views  import OwnersViewSet, PetviewSet, PetDateviewSet 

#Router
router = routers.DefaultRouter()
router.register(r"owners", OwnersViewSet)
router.register(r"pets",PetviewSet)
router.register(r"petsdate", PetDateviewSet)


#ENDPOINTS:
#OWNERS/ -> POST
#owners/ ->  GET
#owners/ -> 
#owners/id -> 
#owners/id ->
urlpatterns = [
    path("",include(router.urls)), 
]
