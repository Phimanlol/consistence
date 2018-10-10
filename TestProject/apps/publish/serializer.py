# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers

from .models import Publish, Comment
from users.serializer import UserForShowSerializer, UserForCommentSerializer
from pet.models import Pet
from pet.serializer import PetsSerializer, PetForPublishSerializer

User = get_user_model()


class PublishForUpdateSerializer(serializers.ModelSerializer):
    pet = PetForPublishSerializer()

    def update(self, instance, validated_data):
        pet_data = validated_data.pop('pet')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        pet = instance.pet
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.province = validated_data.get('province', instance.province)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        pet.adopted = pet_data.get('adopted', pet.adopted)
        pet.save()

        return instance

    class Meta:
        model = Publish
        fields = ('title', 'description', 'publish_time',
                  'pet', 'user','province', 'address', 'id',)
        read_only_fields = ('publish_time',)

class PublishSerializer(serializers.ModelSerializer):
    user = UserForShowSerializer()
    publish_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Publish
        fields = ('title', 'description', 'publish_time',
                  'pet', 'user','province', 'address', 'id',)

class PublishForCreateSerializer(serializers.ModelSerializer):
    """

    发布信息所需要的序列化
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(),)
    pet = PetForPublishSerializer()
    publish_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        pet_data = validated_data.pop('pet')
        pet_data['adopted'] = False    # 发布信息确保宠物处于未被领养状态
        publish = Publish.objects.create(**validated_data)
        Pet.objects.create(publish = publish, **pet_data)
        return publish


    class Meta:
        model = Publish
        fields = ('title', 'description', 'publish_time',
                  'pet', 'user', 'province', 'address', 'id')


class CommentSerializer(serializers.ModelSerializer):
    user = UserForCommentSerializer()
    add_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Publish
        fields = ('user', 'publish', "add_time")


