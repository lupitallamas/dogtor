from django.urls import path, include

#from rest_framework import routers

#Views
#from .views  import OwnersViewSet, PetviewSet, PetDateviewSet 
from .views import ListOwnersAPIView, RetriveOwnersAPIView, CreateOwnersAPIView, UpdateOwnersAPIView, DeleteOwnersAPIView
from .views import RetriveUpdateDestroyOwnerAPIView, ListCreateOwnerAPIView
#Router
#router.register(r"owners", OwnersViewSet)
#router.register(r"pets",PetviewSet)
#router.register(r"petsdate", PetDateviewSet)


#ENDPOINTS:

# owners/ -> POST -> create owner
# owners/ -> GET -> list owners
# owners/id -> GET -> list a owner
# owners/id -> PUT -> update owner
# owners/id -> DELETE -> delete a owner
urlpatterns = [
      path("owners/<int:pk>/", RetriveUpdateDestroyOwnerAPIView.as_view(), name ="owner_retup"),
      path("owners/",ListCreateOwnerAPIView.as_view(), name="owner_lscr"),
      #path("",include(router.urls)),  
      #path("owners/", ListOwnersAPIView.as_view(), name="owners_list"),
      #path("owners/<int:pk>/",RetriveOwnersAPIView.as_view(), name="owners_detail"),
      #path("owners/add",CreateOwnersAPIView.as_view(), name="owner_create"),
      #path("owners/<int:pk>/Update", UpdateOwnersAPIView.as_view(), name="owner_update" ),
      #path("owners/<int:pk>/Delete",DeleteOwnersAPIView.as_view(), name="owner_delete"),
 ]
