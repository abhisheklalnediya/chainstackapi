from Care.models import Care
from rest_framework import generics
from Care.serializers import CareSerializer
from Care.permissions import IsOwnerOrAdmin
from rest_framework.exceptions import PermissionDenied

class CareList(generics.ListCreateAPIView):
    serializer_class = CareSerializer
    
    def get_queryset(self):
        user  = self.request.user

        # all care if owner or super user.
        if(user.is_superuser):
            return Care.objects.all()
        return Care.objects.filter(owner = user)

    def perform_create(self, serializer):
        user = self.request.user
        if user.quota == 0:
            raise PermissionDenied('Not enough quota')
        serializer.save(owner=self.request.user)
        user.quota -= 1
        user.save() 


class CareDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Care.objects.all()
    serializer_class = CareSerializer
