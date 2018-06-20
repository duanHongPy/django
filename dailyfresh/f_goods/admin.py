# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','tname']
class GoodInfoAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ['id','gname','gprice','gunit','gclick','gstock','gtype']
    #每页显示多少项
    list_per_page = 15

admin.site.register(TypeGoods,TypeInfoAdmin)
admin.site.register(GoodInfo,GoodInfoAdmin)