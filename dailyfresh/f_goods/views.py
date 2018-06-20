# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
# from django.http import response
# Create your views here.
def index(request):
    typelist = TypeGoods.objects.all()
    newgoods = typelist[0].goodinfo_set.order_by('-id')[0:4]
    maxgoods = typelist[0].goodinfo_set.order_by('-gclick')[0:4]
    context = {'title':'首页','newgoods':newgoods,'maxgoods':maxgoods}
    return render(request,'f_goods/index.html',context)

#typeid表示类型id ，pid表示当前页数 sortid表示排序方式
def list(request,typyid,pid,sortid):
    typeone = TypeGoods.objects.get(id=int(typyid))
    newgoodslist = typeone.goodinfo_set.order_by('-id')[0:2]

    if sortid == '1':

        goods_list = GoodInfo.objects.filter(gtype_id=int(typyid)).order_by('-id')
    elif sortid == '2':
        goods_list = GoodInfo.objects.filter(gtype=int(typyid)).order_by('-gprice')
    elif sortid == '3':
        goods_list = GoodInfo.objects.filter(gtype=int(typyid)).order_by('-gclick')
    # 分页处理

    #创建分页对象
    p = Paginator(goods_list,10)
    #获取当前页数据

    p_list = p.page(int(pid))
    #获取当前页面个数
    n = len(p_list)
    context = {'title':typeone.tname,'newgoodslist':newgoodslist,'p_list':p_list,'sort':sortid,'typeid':int(typyid),'n':n,'p':p}

    return render(request,'f_goods/list.html',context)

def detail(request,goods_id):
    goods = GoodInfo.objects.get(id=goods_id)
    goods.gclick += 1
    goods.save()
    new = goods.gtype.goodinfo_set.order_by('-id')[0:2]

    #最近浏览功能
    #nowgoods为字符串  nowgoods1为列表
    nowgoods = request.COOKIES.get('nowgoods','')
    goods_id = str(goods.id)
    context = {'title':goods.gname,'goods':goods,'new':new}
    response = render(request,'f_goods/detail.html',context)
    if nowgoods != '':
        nowgoods1 = nowgoods.split(',')
        if nowgoods1.count(goods_id) == 1:
            nowgoods1.remove(goods_id)
        nowgoods1.insert(0,goods_id)
        if len(nowgoods1) == 6:
            del nowgoods1[5]
        #表示以逗号作为分割连接列表中的每个元素组成字符串
        nowgoods = ','.join(nowgoods1)
    else:
        nowgoods = goods_id
    response.set_cookie('nowgoods',nowgoods)

    return response