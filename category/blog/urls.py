from django.conf.urls import url

from . import views
urlpatterns=[
	url(r'^$',views.index),
	url(r'^jurnal/$',views.jurnal),
	url(r'^tutorial/$',views.tutorial)

]