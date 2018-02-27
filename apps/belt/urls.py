from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
		url(r'^home/remove/(?P<id>\d+)$',views.remove),
		url(r'^friend/(?P<id>\d+)$',views.friend),
		url(r'^home/view/(?P<id>\d+)$',views.view),
		url(r'^logout',views.logout),
		url(r'^home/(?P<id>\d+)$',views.home),
		url(r'^login',views.login),
		url(r'^process', views.process),
		url(r'^$', views.index),
		]