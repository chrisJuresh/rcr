from rest_framework import serializers
from .models import Trust

class TrustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trust
        fields = ['id','name']

