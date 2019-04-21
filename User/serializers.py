from User.models import User, QuotaCredit
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'quota')
        read_only_fields = ('quota',)
    
class QuotaCreditSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    class Meta:
        model = QuotaCredit
        fields = ('user', 'credit', )

    