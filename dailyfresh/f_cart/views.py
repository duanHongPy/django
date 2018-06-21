# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from f_cart.models import *

# Create your views here.
def cart(request):
    uid = request.session['user_id']
    cart_goods = CartInfo.objects.filter(user=uid)
    context = {'title':'购物车','cart_goods':cart_goods}

    return render(request,'f_cart/cart.html',context)

def add(request,gid,count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    #查询购物车是否已经有这个用户对应的这个商品
    cart = CartInfo.objects.filter(goods=gid,user=uid)
    if len(cart) == 1:
        cart_new = cart[0]
        cart_new.count += count
    else:
        cart_new = CartInfo()
        #添加外键使用 列名_id的形式
        cart_new.goods_id = gid
        cart_new.user_id = uid
        cart_new.count = count

    cart_new.save()
    return redirect('/fresh/cart')