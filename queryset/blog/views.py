from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
	posts = Post.objects.all()
	context = {
	'judul':'blog',
	'heading':'selamat datang di blog',
	'Posts':posts
	}

	return render(request,'index.html',context)

def berita(request,input):
	posts = Post.objects.filter(category='berita')
	context = {
	'judul':'blog',
	'heading':'selamat datang di blog',
	'Posts':posts,
	'category':'berita'
	}

	return render(request,'index.html',context)


def jurnal(request):
	posts = Post.objects.filter(category='jurnal')
	context = {
	'judul':'blog',
	'heading':'selamat datang di blog',
	'Posts':posts,
	'category':'jurnal'
	}

	return render(request,'index.html',context)

def gosip(request):
	posts = Post.objects.filter(category='gosip')
	context = {
	'judul':'blog',
	'heading':'selamat datang di blog',
	'Posts':posts,
	"category":'gosip'
	}

	return render(request,'index.html',context)