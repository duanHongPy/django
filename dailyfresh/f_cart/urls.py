from django.conf.urls import url
import views

urlpatterns = [
   url(r'^cart$',views.cart),
    url(r'^add_(\d+)_(\d+)$',views.add),
]