from rest_framework import serializers

#Modelos
from vet.models import PetOwner, Pet, PetDate

class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owers serializer."""
    
    
    class Meta:
        model= PetOwner
        fields= [
                "id",
                "first_name",
                "last_name",
                "email",
                "address",
                "phone",
                "created_at",
            
        ]
class PetsSerializers(serializers.HyperlinkedModelSerializer):
    """Pet model serializer."""
    
    class Meta:
        model= Pet
        fields = [
            "id",
            "name",
            "type",
        ]    
class PetdateSerializer(serializers.HyperlinkedModelSerializer):
    """Petdate model serializer."""
    
    class Meta:
        model = PetDate
        fields = [
            "datetime",
            "type",
            "created_at",
        ]
              