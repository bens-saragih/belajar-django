from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^(?P<input>[0-9]+)/$',views.berita),
	url(r'^gosip/$',views.gosip),
	url(r'^jurnal/$',views.jurnal)

]