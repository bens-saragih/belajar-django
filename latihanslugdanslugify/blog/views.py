from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post

def index(request):

	return HttpResponse("home blog")

def terserah(request,terserahInput):
	posts = Post.objects.filter(category=terserahInput)
	isi = "<p>{}</p>".format(terserahInput)
	return HttpResponse(isi)

def singlePost(request,slugInput):
	posts = Post.objects.get(slug=slugInput)# artinya ambil slug sama dengan slug yang di ketik di url yang dimana yang ketik adalah judul

	judul = "<h1>{}</h1>".format(posts.judul)
	body = "<p>{}</p>".format(posts.body)
	category ="<p>{}</p>".format(posts.category)
	slug = "<p>{}</p>".format(posts.slug)

	return HttpResponse(judul+body+category+slug)

