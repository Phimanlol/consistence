# -*- coding: UTF-8 -*-
import xadmin
from .models import Publish

class PublishAdmin(object):
    list_display = ['title', 'description', 'publish_time', 'pet', 'user', 'province', 'address']
    search_field = ['user', 'province']
    list_editable = ['title', 'description', 'publish_time', 'pet', 'user', 'province', 'address']
    list_filter = ['title', 'description', 'pet', 'user', 'province', 'address']


xadmin.site.register(Publish, PublishAdmin)
