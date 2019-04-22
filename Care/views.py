from Care.models import Care
from rest_framework import generics
from Care.serializers import CareSerializer
from Care.permissions import IsOwnerOrAdmin
from rest_framework.exceptions import PermissionDenied

class CareList(generics.ListCreateAPIView):
    """
        get:
        Return a list of care items owned by the user. if the user is admin all care items are shown.

        post:
        Create a care item. Checks for quota avaliablity, if quota is limited then quota will be reduced by 1 for each created care item. 
        New users have unlimited quota. If Quota is exhausted, the API will throw a 403 error.
    """

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
            raise PermissionDenied('Not enough quota available')
        serializer.save(owner=self.request.user)
        user.quota -= 1
        user.save() 


class CareDetail(generics.RetrieveDestroyAPIView):
    """
        get:
        Return a details about a care item. Care Item should be owned by the user.
        
        delete:
        Delete a care item, Quota used for this item will not be reverted
    """
    permission_classes = [IsOwnerOrAdmin]
    queryset = Care.objects.all()
    serializer_class = CareSerializer
