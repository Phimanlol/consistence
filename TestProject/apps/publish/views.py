from django.shortcuts import render

# Create your views here.

from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.viewsets import  GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin

from utils.permissions import IsOwnerOrReadOnly

from .models import Publish, Comment
from .serializer import PublishSerializer, PublishForCreateSerializer, PublishForUpdateSerializer, CommentSerializer

from TestProject.celery import app

class PublishViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return PublishForCreateSerializer
        if self.action == 'update':
            return PublishForUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [permission() for permission in self.permission_classes]
        if self.action == 'update':
            return  (IsOwnerOrReadOnly(), )
        return (permissions.AllowAny(), )


    def retrieve(self, request, *args, **kwargs):
        """
        如果是匿名用户访问该信息：
        则宠物主人的手机号被隐藏,并提示其需登陆查看
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not self.request.user.is_authenticated():
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            original_data = serializer.data
            mobile = original_data['user']['mobile']
            # hidden_mobile = mobile[:4] + '****' + mobile[8:] 如果项目是要求是用户手机号必填的话:
            #                                                  隐藏号码中间四位，我的项目无此要求:
            #                                                  如果用户没绑定手机号，此段代码会报错:
            #                                                  'NoneType' object is not subscriptable

            hidden_mobile = '请登陆查看此用户的联系方式'
            serializer.data['user']['mobile'] = hidden_mobile
            return Response(serializer.data)
        return super(PublishViewSet,self).retrieve(request, *args, **kwargs)

    def validate(self):
        if self.action == 'create':
            user = self.request.user
            if user.category != 'out':
                raise serializers.ValidationError('你是宠物收养用户，无法发布宠物信息')


class CommentViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializers = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        if self.action == 'retrieve':
            return self.queryset.filter(user=self.request.user)







