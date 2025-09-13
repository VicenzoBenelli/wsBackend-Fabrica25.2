from rest_framework import serializers
from .models import Filme, CustomUser, Resenha


class CustomUserSerializer(serializers.ModelSerializer):
    resenhas_ids = serializers.PrimaryKeyRelatedField(queryset=Resenha.objects.all(), many=True, required=False, allow_empty=True)
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "resenhas_ids",
            "password" 
        ]
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_resenhas_ids(self, value):
     if value == "" or value is None:
        return []
     return value

    def create(self, validated_data):
        resenhas = validated_data.pop("resenhas_ids", [])
        password = validated_data.pop("password", None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)  
        user.save()

        if resenhas:
            user.resenhas_ids.set(resenhas)
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


class ResenhaSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = Resenha
        fields = '__all__'

    


    







        
