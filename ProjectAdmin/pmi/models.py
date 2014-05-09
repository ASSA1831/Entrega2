from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    Comienzo_pro = models.DateTimeField('Fecha de inicio')
    final_pro= models.DateTimeField('Fecha final')
    def __str__(self):  
        return self.nombre
        
class Tarea(models.Model):
    nombre= models.CharField(max_length=100)
    comienzo= models.DateTimeField('Fecha de inicio')
    final= models.DateTimeField('Fecha final')
    proyecto= models.ForeignKey(Proyecto)
    def __str__(self):  
        return self.nombre

# Create your models here.
