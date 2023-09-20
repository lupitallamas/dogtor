from django.db import models


from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from  .managers import ModUserManager

# Create your models here.
#Manager
class ModUser(AbstractBaseUser,PermissionsMixin):
    """Custom Moderator User."""
  #Sobreescribir propiedades del modelo User    
  #Extender (nuevos fiels)
  
    email = models.EmailField(unique=True)
    user_name= models.CharField(max_length=150,unique=True)
    first_name= models.CharField(max_length=50, unique=True)
    star_date= models.DateTimeField(auto_now_add=True)    
    about =models.TextField(max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = ModUserManager()
    #Campo_identificador del user
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "first_name"]
    #Metodo string
    def __str__(self):
        return f"{self.user_name} {self.email}"
    
    
    