from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from .models import UserModel
from .permissions import IsSuperUser
from .serializers import AddAvatarSerializer, UserSerializer


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return IsSuperUser(),
        return super().get_permissions()


class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer
    http_method_names = ('patch',)

    def get_object(self):
        return self.request.user.profile
