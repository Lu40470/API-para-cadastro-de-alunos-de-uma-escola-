from rest_framework import serializers
from .models import cursos,avaliações
from django.db.models import Avg

class avaliaçõesSerializer(serializers.ModelSerializer): 

    class Meta: 
        extra_kwargs = {'email':{'write_only': True}}

        model = avaliações
        fields = ['id','curso','nome','email','comentario','avaliação','criação','ativo']
    def validate_avaliação(self,valor):
        if valor in range(1,5):
            return valor
        raise serializers.ValidationError('Por favor, insira um número no intervalor de 1-5')

#1 Nested relationship
'''avaliações = avaliaçõesSerializer(many = True, read_only = True)'''
#2 Hyperlinked Related field 
'''class cursosSerializer(serializers.ModelSerializer): 
    avaliações = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name = 'avaliações-detail')
    class Meta:
        model = cursos
        fields =['id','titulo','url','criação','ativo','avaliações']'''
#3 - Primary key
class cursosSerializer(serializers.ModelSerializer): 
    avaliações = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    media_avaliações = serializers.SerializerMethodField()
    class Meta:
        model = cursos
        fields =['id','titulo','url','criação','ativo','avaliações','media_avaliações']

    def get_media_avaliações(self,obj):
        media = obj.avaliações.aggregate(Avg('avaliação')).get('avaliação__avg')
        if media is None:
            return 0
        return round(media*2)/2
