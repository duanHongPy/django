# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20,unique=True)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30,unique=True)
    ushou = models.CharField(max_length=10,default='')
    uaddressee = models.CharField(max_length=20,default='')
    upost = models.CharField(max_length=6,default='')
    uphone = models.CharField(max_length=11,default='')
    #default、blank是python层面的约束，不影响数据库表结构
    #blank 为true允许该字段为空白，默认为false