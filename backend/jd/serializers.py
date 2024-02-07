from rest_framework import serializers
from .models import JD

class JDSerializer(serializers.ModelSerializer):
    class Meta:
        model = JD
        fields = ['document', 'submission_date', 'trust']

    def create(self, validated_data):
        user = self.context['request'].user
        trust = user.trust
        if not trust:
            raise serializers.ValidationError("A trust must be associated with the user to submit a JD.")
        jd = JD.objects.create(trust=trust, **validated_data)
        return jd