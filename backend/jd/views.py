from django.shortcuts import render
from rest_framework import viewsets
from .models import JD
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import JDSerializer, JDReadSerializer  

class JDViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return JD.objects.filter(trust=user.trust)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return JDReadSerializer
        return JDSerializer