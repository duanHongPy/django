from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^list_(\d+)_(\d+)_(\d+)$',views.list),
    url(r'^(\d+)$',views.detail),
    url(r'^pag(?P<pIndex>[0-9]*)/$', views.list, name='pagTest'),
]