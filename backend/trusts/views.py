from django.shortcuts import render
from .models import Trust
from rest_framework import viewsets
from trusts.serializers import TrustSerializer

class TrustViewSet(viewsets.ModelViewSet):
    queryset = Trust.objects.all()
    serializer_class = TrustSerializer