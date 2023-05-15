from rest_framework import serializers
from unissApp.models import *

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profesor
        fields ='__all__'
        