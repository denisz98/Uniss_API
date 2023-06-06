from rest_framework import routers
from django.urls import path
from unissApp.viewsets import *

router = routers.SimpleRouter()
router.register('profesor', ProfesorViewSet)
router.register('estudiante', EstudianteViewSet)

urlpatterns = router.urls
