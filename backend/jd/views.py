from django.shortcuts import render
from rest_framework import viewsets
from .models import JD
from .serializers import JDSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class JDViewSet(viewsets.ModelViewSet):
    queryset = JD.objects.all()
    serializer_class = JDSerializer