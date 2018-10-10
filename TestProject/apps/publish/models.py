
# Create your models here.


from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.utils import timezone

from pet.models import Pet
from users.models import Users

# Create your models here.

User = get_user_model()


class Publish(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField('宠物描述', max_length=500, null=True, blank=True)
    publish_time = models.DateField('发布时间', default=now)
    pet = models.OneToOneField(Pet, related_name='publish', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='宠物主人', default='', related_name='publish_set')
    province = models.CharField('省份', max_length=10, null=True, blank=True)
    address = models.CharField('详细地址', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "领养信息"
        verbose_name_plural = "领养信息"
        ordering=('-publish_time',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """

    信息评论系统
    """
    user = models.ForeignKey(User, verbose_name="用户")
    publish = models.ForeignKey(Publish,verbose_name="发布信息")
    add_time = models.DateTimeField("评论发布时间", auto_now_add=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering = ("-add_time", )

    def __str__(self):
        return "{0.publish.title}的评论".format(self)
