
from django.contrib.auth import get_user_model

from rest_framework import mixins, permissions
from rest_framework import viewsets

from .serializer import UserRegisterSerializer, UserForShowSerializer

from .tasks import send_mobile_message

User = get_user_model()

# Create your views here.


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户的信息展示，不能删除用户
    """
    queryset = User.objects.all()
    serializer_class = UserForShowSerializer

    def perform_create(self, serializer):
        """

        用户注册成功，通过celery发短信放入消息队列
        :param serializer:
        :return:
        """
        send_mobile_message.delay()
        serializer.save()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        return UserForShowSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny(),]
        return [permissions.IsAuthenticated()]

    def get_object(self):
        return self.request.user




