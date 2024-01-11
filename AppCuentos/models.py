from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cuento(models.Model):
    # autor = models.ForeignKey(User, on_delete=models.CASCADE)
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=1000)
    puntuacion = models.IntegerField(default=0)

class Historia(models.Model):
    autor = models.CharField(max_length=200, help_text="Nombre del autor o autores de la historia")
    titulo = models.CharField(max_length=200, help_text="Título de la historia")
    contenido = models.TextField(help_text="Contenido de la historia")
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación de la historia")
    puntuacion = models.IntegerField(default=0, help_text="Puntuación de la historia")



class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')
    biografia = models.TextField()

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuento = models.ForeignKey(Cuento, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class HistoriaComun(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
