from User.models import User, QuotaCredit
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'quota', "password")
        read_only_fields = ('quota',)
    
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["email"], **validated_data)
        return user
    
class QuotaCreditSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    class Meta:
        model = QuotaCredit
        fields = ('user', 'credit', )

    