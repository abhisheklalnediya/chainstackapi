from User.models import User, QuotaCredit
from rest_framework import generics
from User.serializers import UserSerializer, QuotaCreditSerializer
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListCreateAPIView):
    """
        post:
        Creates a new user with email and password. Only Admin can access this endpoint.
        get:
        Get list of all users. Only Admin can access this endpoint.
    """
    permission_classes = [ IsAdminUser ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveDestroyAPIView):
    """
        delete:
        Deletes a user, All the care items he created will also be deleted. Only Admin can access this endpoint.
        get:
        Get details about a user. Only Admin can access this endpoint.
    """
    permission_classes = [ IsAdminUser ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuotaCreditList(generics.ListCreateAPIView):
    """
        post:
        Credit a user with quota. This will move the user form unlimited quota to limited quota.
        Accepts user's id and the number of quotas to be credited. Only Admin can access this endpoint
        get:
        List all the quota credits for all users. Only Admin can access this endpoint.
    """
    permission_classes = [ IsAdminUser ]
    queryset = QuotaCredit.objects.all()
    serializer_class = QuotaCreditSerializer