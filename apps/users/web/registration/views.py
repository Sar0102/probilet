from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.users.models import User
from apps.users.web.registration.serializers import UserSerializer


class CreateUserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []
