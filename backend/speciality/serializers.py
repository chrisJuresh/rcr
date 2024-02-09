from rest_framework import serializers
from .models import Speciality

class SpecialitySerializer(serializers.ModelSerializer):
    consultant_type_name = serializers.SerializerMethodField()

    class Meta:
        model = Speciality
        fields = ['id', 'name', 'consultant_type', 'consultant_type_name']

    def get_consultant_type_name(self, obj):
        return obj.consultant_type.name