from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import FilmeSerialaizers, ResenhaSerialaizers, CustomUserSerializer
from .models import Filme, Resenha, CustomUser
from .permissions import IsOwnerOrReadOnly
import requests
from datetime import datetime
from rest_framework import serializers


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerialaizers
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        titulo = serializer.validated_data.get('title')
        if not titulo:
            raise serializers.ValidationError({"title": "O título é obrigatório."})

        api_key = "38122092"
        url = f"http://www.omdbapi.com/?t={titulo.strip()}&apikey={api_key}"

        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            raise serializers.ValidationError({"erro": f"Falha ao acessar OMDb API: {e}"})

        data = resp.json()

        if data.get("Response") == "False":
            raise serializers.ValidationError({"erro": "Filme não encontrado na OMDb."})

        year = int(data["Year"]) if data.get("Year") and data["Year"].isdigit() else None

        released = None
        if data.get("Released") and data["Released"] != "N/A":
            try:
                released = datetime.strptime(data["Released"], "%d %b %Y").date()
            except ValueError:
                released = None

        runtime_minutes = None
        if data.get("Runtime") and "min" in data.get("Runtime"):
            try:
                runtime_minutes = int(data["Runtime"].replace(" min", ""))
            except ValueError:
                runtime_minutes = None

        serializer.save(
            year=year,
            rated=data.get("Rated") if data.get("Rated") != "N/A" else None,
            released=released,
            runtime_minutes=runtime_minutes,
            genre=data.get("Genre") if data.get("Genre") != "N/A" else None,
            director=data.get("Director") if data.get("Director") != "N/A" else None,
            writer=data.get("Writer") if data.get("Writer") != "N/A" else None,
            actors=data.get("Actors") if data.get("Actors") != "N/A" else None,
            poster=data.get("Poster") if data.get("Poster") != "N/A" else None,
        )


class ResenhaViewSet(viewsets.ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerialaizers
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Aqui usamos o nome real do campo no model: user_id
        serializer.save(user_id=self.request.user)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
