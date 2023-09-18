from django.contrib import admin
#
from . import models  #Se importan todos los modelos
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """PostAdmin model for admin"""
    #name es el nombre del campo del modelo post
    fields=["name"]

#Este es el sitio Panel de administracion par la app de 'blog'
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel adminstraction"""
    site_header = "Blog Site Admin Area"


    
#instancear=llamar se hizo la class 'BlogAdminArea' y la instanciamos aquí   es utilizarla
blog_admin_site =BlogAdminArea(name="BlogAdmin")


#Esta es una forma de poner en el admin la app dependiente del admin general, si las quido puedo usar decoradores por eso estan comentadas
#Registramos modelo Post en nuestro admin area
#el segundo parametro es la class que se hizo arriba de PostAdmin, son los campos que quiero que se vea en el admin 
#****ojo** blog_admin_site.register(models.Post, PostAdmin)
#con este instruccion añadimos los modelos Post al admin General. Si no lo pongo entonces queda como independiente
#****ojo** admin.site.register(models.Post, PostAdmin)
