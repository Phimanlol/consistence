# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from pet.serializer import PetForPublishSerializer
User = get_user_model()




class UserForShowSerializer(serializers.ModelSerializer):
    """

    宠物，及发布信息所使用的用户数据
    """
    class Meta:
        model = User
        fields = ('name', 'gender', 'mobile')


class UserRegisterSerializer(serializers.ModelSerializer):
    """

    用户注册使用
    """

    username = serializers.CharField(max_length=11,
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message='该用户名又被注册')])
    password = serializers.CharField(write_only=True,
                                     min_length=8,
                                     required=True,
                                     style={'input_type': 'password'})

    def create(self, validated_data):
        instance = super(UserRegisterSerializer, self).create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('username', 'password', 'gender', 'mobile', 'category',)

class UserForCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'gender')




