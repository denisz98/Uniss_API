from rest_framework import serializers
from unissApp.models import *

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profesor
        fields ='__all__'
        
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Estudiante
        fields ='__all__'
        