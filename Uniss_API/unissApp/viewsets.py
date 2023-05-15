from rest_framework import viewsets
from unissApp.models import *
from unissApp.serializer import *

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer