from django.db import models

# Create your models here.
class Post(models.Model):
    """Model post."""
    name= models.CharField(max_length=50)
    description= models.TextField(max_length=1000, blank=True, null=True)
    #blank=nulo a nivel de formulario django
    #null=nulo a nivel de BD, nivel postgres
    def __str__(self):
        return  f"{self.pk} {self.name}"  
    