from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serialaizers import *
from .models import *

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerialaizers

class ResenhaViewSet(viewsets.ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerialaizers
  

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer