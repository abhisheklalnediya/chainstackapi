from Care.models import Care
from rest_framework import serializers

class CareSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Care
        fields = ('id', 'name', 'owner')