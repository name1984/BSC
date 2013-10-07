from django.db import models

# Create your models here.

class  mision(models.Models):
    descripcion= models.CharField(max_lenght=50)
    empresa= models.CharField(max_lenght=20)
    
    def __unicode__(self):
        return self.nombre
