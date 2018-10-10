# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class Users(AbstractUser):
    Gender_Choices = (
        ('male', '先生'),
        ('female', '女士')
    )

    User_Choices = (
        ('out', '宠物领养'),
        ('in', '宠物送养')
    )

    name = models.CharField('姓名', max_length=30, null=True, blank=True)
    gender = models.CharField('性别', choices=Gender_Choices,max_length=6)
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True, editable=True)
    category = models.CharField('是否领养', choices=User_Choices, max_length=10, default='out')
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username

