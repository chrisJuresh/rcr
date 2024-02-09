from rest_framework import serializers
from jd.models import JD
from speciality.models import Speciality, ConsultantType

class JDSerializer(serializers.ModelSerializer):
    primarySpecialities = serializers.PrimaryKeyRelatedField(queryset=Speciality.objects.all(), many=True)
    subSpecialities = serializers.PrimaryKeyRelatedField(queryset=Speciality.objects.all(), many=True)

    consultantType = serializers.SlugRelatedField(slug_field='name', queryset=ConsultantType.objects.all())

    class Meta:
        model = JD
        fields = ['document', 'submission_date', 'trust', 'consultantType','primarySpecialities', 'subSpecialities']

    def create(self, validated_data):
        primary_specialities = validated_data.pop('primarySpecialities', [])
        sub_specialities = validated_data.pop('subSpecialities', [])
        jd = JD.objects.create(**validated_data)
        jd.primarySpecialities.set(primary_specialities)
        jd.subSpecialities.set(sub_specialities)
        return jd

class SpecialityNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class JDReadSerializer(serializers.ModelSerializer):
    primarySpecialities = SpecialityNameField(many=True, queryset=Speciality.objects.all())
    subSpecialities = SpecialityNameField(many=True, queryset=Speciality.objects.all())
    consultantType = serializers.CharField(source='consultantType.name')

    class Meta:
        model = JD
        fields = ['id', 'document', 'submission_date', 'trust', 'consultantType', 'primarySpecialities', 'subSpecialities']