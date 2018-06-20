# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
from .models import *
from . import user_decorator
from f_goods.models import GoodInfo
# Create your views here.
def register(request):
    context = {'title':'用户注册'}
    return render(request,'f_user/register.html',context)

def register_handle(request):
    #接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断二次密码是否一样
    if upwd != upwd2:
        return redirect('/fresh/register/')
    #密码加密
    s = sha1()
    s.update(upwd)
    upwd3 = s.hexdigest()
    # #创建模板对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #注册成功转到登陆页面
    return redirect('/fresh/login/')

#检测用户名是否存在
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

#检测邮箱是否存在
def register_exist_email(request):
    uemail = request.GET.get('email')
    count = UserInfo.objects.filter(uemail=uemail).count()
    return JsonResponse({'count':count})

#登录
def login(request):
    uname = request.COOKIES.get('uname','1')
    context = {'title':'用户登录','username':uname,'error_name':0,'error_pwd':0}
    return render(request,'f_user/login.html',context)

def login_handle(request):
    #接收请求信息
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    #页面勾选记住密码 则jizhu 的值为1,不勾选则为空
    jizhu = request.POST.get('jizhu',0)
    #根据用户信息查对象
    #filter查询为空返回[]，get查询为空返回异常
    user = UserInfo.objects.filter(uname=uname)
    print(user)
    if len(user) == 1:
        s = sha1()
        s.update(upwd)
        upwd2 = s.hexdigest()
        if upwd2 == user[0].upwd:
            url = request.COOKIES.get('url','/fresh/')
            re = HttpResponseRedirect(url)
            #post接收到的均为字符串
            if jizhu != 0:
                re.set_cookie('uname',uname)
            else:
                re.set_cookie('uanme','',max_age = -1)
            #将常用的变量存到session中
            request.session['user_id'] = user[0].id
            request.session['username'] = user[0].uname
            return re
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'username':uname,'pwd':upwd}
            return render(request,'f_user/login.html',context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0,'username':uname,'pwd':upwd}
        return render(request, 'f_user/login.html', context)

#个人信息页面

@user_decorator.loginyanzheng
def info(request):
    uemail = UserInfo.objects.get(id=request.session['user_id']).uemail
    uphone = UserInfo.objects.get(id=request.session['user_id']).uphone
    uadress = UserInfo.objects.get(id=request.session['user_id']).uaddressee

    #最近浏览
    nowgoods = request.COOKIES.get('nowgoods','')
    goodlist = []
    if nowgoods != '':
        nowgoodslist = nowgoods.split(',')

        for g in nowgoodslist:
            goodlist.append(GoodInfo.objects.get(id=int(g)))

    context = {'action':1,'title':'个人中心','uname':request.session['username'],'uemail':uemail,'uphone':uphone,'uadress':uadress,
               'goodslist':goodlist}
    return render(request,'f_user/user_center_info.html',context)

def loginout(request):
    #清除会话 删除当前的会话数据并删除会话的Cookie
    request.session.flush()
    return HttpResponseRedirect('/fresh/')

@user_decorator.loginyanzheng
def order(request):
    context = {'action':2,'title':'个人中心'}
    return render(request,'f_user/user_center_order.html',context)

@user_decorator.loginyanzheng
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        user.uaddressee = request.POST.get('uadress')
        user.ushou = request.POST.get('ushou')
        user.uphone = request.POST.get('uphone')
        user.upost = request.POST.get('upost')
        user.save()
    context = {'action':3,'title':'个人中心','user':user}
    return render(request,'f_user/user_center_site.html',context)


