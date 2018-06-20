# -*- coding: utf-8 -*-
#登录验证
from django.http import HttpResponseRedirect

def loginyanzheng(fun):
    def login_fun(request,*args,**kwargs):
        #request.session['id'] 如果id不存在会报错
        if request.session.has_key('user_id'):
            return fun(request,*args,**kwargs)
        else:
            re = HttpResponseRedirect('/fresh/login')
            re.set_cookie('url',request.get_full_path())
            return re
    return login_fun

#request.get_full_path()和re.path
# http://127.0.0.1:8000/200/?type=1
# request.get_full_path()表示/200/？type=1
# re.path表示/200/
