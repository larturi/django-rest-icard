from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from users.models import User
from .serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()