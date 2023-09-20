from django.contrib.auth.models import BaseUserManager


class ModUserManager(BaseUserManager):
    """Mod User Custom Manager."""
    
    #1. create_use
    # miren->12345678#
    def create_user(self,email, user_name, first_name, password, **other_fields):
        """Overriding crate_user func for ModUserManager"""
         
        #Agregar Validaciones
        if not email:
            raise ValueError("You must privide an email...")
        #Ponemos en minuscula el dominio
        email =self.normalize_email(email)
        user = self.model(
            email=email,user_name=user_name,first_name=first_name,**other_fields
        )
        #Seteamos password
        user.set_password(password)
        
        #Guardar en BD
        user.save()
        return user
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """Overriding create_superuser func for MoUseManager."""
    
        #is_staff->Verdadero
        #is_active -> Verdadero
        #is_superuser -> Verdadero
    
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active",True)
        other_fields.setdefault("is_superuser", True)
        #Cramos el usuario con la funcion recien cread de create_uset
        return self.create_user(email, user_name, first_name, password,**other_fields)
    #2. crate_superuser
    #admin-ª123456
   