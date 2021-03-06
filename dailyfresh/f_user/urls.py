from django.conf.urls import url
from f_user import views

urlpatterns = [
    url(r'^register$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exist/$',views.register_exist),
    url(r'^register_exist_email/$',views.register_exist_email),
    url(r'^login$',views.login),
    url(r'^login_handle$',views.login_handle),
    url(r'^info$',views.info),
    url(r'^order$',views.order),
    url(r'^site$',views.site),
    url(r'^loginout$',views.loginout)
]