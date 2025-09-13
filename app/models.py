from django.db import models
from django.contrib.auth.models import AbstractUser


class Filme(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(null=True, blank=True)
    rated = models.CharField(max_length=20, null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    runtime_minutes = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    director = models.CharField(max_length=200, null=True, blank=True)
    writer = models.TextField(null=True, blank=True)
    actors = models.TextField(null=True, blank=True)
    poster = models.URLField(max_length=1000, null=True, blank=True) 

    def __str__(self):
        return self.title 


class CustomUser(AbstractUser):

    resenhas_ids = models.ManyToManyField('Resenha', blank= True, related_name='usuarios')




class Resenha(models.Model):
    nome = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    filme_id = models.ForeignKey('Filme', on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(max_length=300)

    def __str__(self):
        return self.nome  


  
