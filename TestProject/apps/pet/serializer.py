# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Pet

User = get_user_model()
class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('age', 'type', 'adopted', 'size', 'photo',)

class PetForPublishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('age', 'type', 'adopted', 'size', 'photo',)






