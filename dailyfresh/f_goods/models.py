# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeGoods(models.Model):
    tname = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.tname.encode('utf-8')

class GoodInfo(models.Model):
    gname = models.CharField(max_length=20)
    #upload_to表示上传目录
    gpic = models.ImageField(upload_to='f_goods')
    #浮点数总位数5，小数2位
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    # 单位
    gunit = models.CharField(max_length=20,default='500g')
    #人气 即点击数
    gclick = models.IntegerField(default=0)
    #简介
    gjianjie = models.CharField(max_length=200)
    #库存
    gstock = models.IntegerField()
    #介绍
    gcontent = HTMLField()
    #销量
    gsales = models.IntegerField
    gtype = models.ForeignKey(TypeGoods)
    #是否广告推荐
    gadv = models.BooleanField(default=False)
