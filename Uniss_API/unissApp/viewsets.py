from rest_framework import viewsets,status
from unissApp.models import *
from unissApp.serializer import *
from rest_framework.settings import api_settings
from rest_framework.response import Response

from unissApp.baseViewSet import *

class ProfesorViewSet(GenericViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    model = Profesor
    id = 'idProfesor'
    
class EstudianteViewSet(GenericViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    model = Estudiante
    id = 'idEstudiante'
    








# class ProfesorViewSet(viewsets.GenericViewSet):
#     queryset = Profesor.objects.all()
#     serializer_class = ProfesorSerializer
    
#     def get_success_headers(self, data):
#         try:
#             return {'Location': str(data[api_settings.URL_FIELD_NAME])}
#         except (TypeError, KeyError):
#             return {}
        
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
    
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         if getattr(instance, '_prefetched_objects_cache', None):
#             instance._prefetched_objects_cache = {}
#         return Response(serializer.data)
    
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if instance is not None:
#             instance.delete()
#             return Response({'message':f'Profesor eliminado correctamente!'},status=status.HTTP_204_NO_CONTENT)
#         return Response({'error':f'No existe un objeto con ese id'}, status=status.HTTP_404_NOT_FOUND)
    