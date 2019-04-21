from User.models import User, QuotaCredit
from rest_framework import generics
from User.serializers import UserSerializer, QuotaCreditSerializer
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListCreateAPIView):
    permission_classes = [ IsAdminUser ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [ IsAdminUser ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuotaCreditList(generics.ListCreateAPIView):
    permission_classes = [ IsAdminUser ]
    queryset = QuotaCredit.objects.all()
    serializer_class = QuotaCreditSerializer