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
        read_only_field= ["create_at",]
class PetsSerializers(serializers.HyperlinkedModelSerializer):
    """Pet model serializer."""
    #queryset=Pet.objects.all()
    owner = serializers.PrimaryKeyRelatedField(
        queryset=PetOwner.objects.all(), many=False
        )
    class Meta:
        model= Pet
        fields = [
            "id",
            "name",
            "type",
            "owner",
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
class OwnersListSerializer(serializers.ModelSerializer):
    """Serializer to list all Pet Owners"""
    class Meta:
        model = PetOwner
        fields = ["id","first_name","last_name"]
        
class OwnersDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""
    class Meta:
        model = PetOwner
        fields = "__all__"

                