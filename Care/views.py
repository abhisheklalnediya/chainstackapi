from Care.models import Care
from rest_framework import generics
from Care.serializers import CareSerializer
from Care.permissions import IsOwnerOrAdmin

class CareList(generics.ListCreateAPIView):
    serializer_class = CareSerializer
    
    def get_queryset(self):
        user  = self.request.user

        # all care if owner or super user.
        if(user.is_superuser):
            return Care.objects.all()
        return Care.objects.filter(owner = user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CareDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Care.objects.all()
    serializer_class = CareSerializer
