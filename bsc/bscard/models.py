from django.db import models

# Create your models here.

class  mision(models.Model):
    descripcion= models.CharField(max_length=50)
    empresa= models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.descripcion
