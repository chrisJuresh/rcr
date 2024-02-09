from rest_framework import serializers
from .models import JD

class JDSerializer(serializers.ModelSerializer):
    class Meta:
        model = JD
        fields = ['document', 'submission_date', 'trust']
