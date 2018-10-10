# -*- coding: utf-8 -*-
import os
from django.db import models
from django.utils.timezone import now
from users.models import Users


# Create your models here.

def upload_to(instance, image):
    image_name, image_ext = os.path.splitext(image)
    return "pet/pet_{2}/{0!s}{1!s}".format(now().strftime('%Y%m%d%H%M%S'),
                                            image_ext.lower(),
                                            instance.id)


class Pet(models.Model):
    name = models.CharField('宠物名称', max_length=10, default='宠物')
    age = models.CharField('年龄', max_length=15, null=True, blank=True)
    user = models.ForeignKey(Users, verbose_name="宠物主人", null=True, blank=True)
    type = models.CharField('宠物类型', max_length=3,
                            choices=(('cat', '猫'), ('dog', '狗'))
                            )
    adopted = models.BooleanField('已被领养', default=False)
    size = models.CharField('尺寸', max_length=6,
                            choices=(("large", "大型"), ('medium', '中等体型'), ('small', '小型'))
                            )
    photo = models.ImageField('图片', upload_to=upload_to, blank=True, null=True)
    add_time = models.DateField('添加时间', default=now)

    class Meta:
        verbose_name = "宠物"
        verbose_name_plural = "宠物"
        ordering = ('-add_time',)

    def __str__(self):
        return self.name






