from django.shortcuts import render
from rest_framework import viewsets
from .models import JD
from .serializers import JDSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class JDViewSet(viewsets.ModelViewSet):
    serializer_class = JDSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return JD.objects.filter(trust=user.trust)