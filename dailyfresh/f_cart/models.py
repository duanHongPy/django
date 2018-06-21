# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CartInfo(models.Model):
    #在不同应用引用模型类的时候需要加应用名前缀
    goods = models.ForeignKey('f_goods.GoodInfo')
    user = models.ForeignKey('f_user.UserInfo')
    #购买商品的数量
    count = models.IntegerField()