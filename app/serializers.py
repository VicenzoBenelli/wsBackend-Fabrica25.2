from rest_framework import serializers
from .models import Filme, CustomUser, Resenha

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password"
        ]
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            del validated_data['password']
        return super().update(instance, validated_data)



class FilmeSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'
        read_only_fields = [
            'id', 'year', 'rated', 'released',
            'runtime_minutes', "genre", "director",
            "writer", "actors", "poster"
        ]


class ResenhaSerialaizers(serializers.ModelSerializer):
    # Nome do usuário logado (somente leitura)
    user = serializers.CharField(source='user_id.username', read_only=True)
    # Nome do filme (somente leitura)
    filme = serializers.CharField(source='filme_id.title', read_only=True)
    # Campo para enviar o ID do filme no POST/PUT (somente escrita)
    filme_id = serializers.PrimaryKeyRelatedField(
        queryset=Filme.objects.all(),
        write_only=True
    )
    # Renomeando campos do modelo
    titulo_da_resenha = serializers.CharField(source='nome')
    resenha = serializers.CharField(source='descricao')

    class Meta:
        model = Resenha
        fields = [
            'id',                # 1º
            'titulo_da_resenha', # vem de nome
            'filme',             # nome do filme (read-only)
            'filme_id',          # id do filme (write-only)
            'nota',              # campo original
            'resenha',           # vem de descricao
            'user'               # nome do usuário (read-only)
        ]
