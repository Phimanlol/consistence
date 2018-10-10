# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from TestProject.celery import app

@app.task
def send_mobile_message(*args, **kwargs):
    """

    用户注册成功，发送手机短信通知
    :param args:
    :param kwargs:
    :return:
    """
    pass