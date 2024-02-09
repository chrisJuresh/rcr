from rest_framework import viewsets
from .models import Speciality
from .serializers import SpecialitySerializer

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer