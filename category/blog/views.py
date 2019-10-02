from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
	post = Post.objects.all()
	context={
	'judul':'blog',
	'heading':'selamat datang',
	'posts':post
	}

	return render(request,'index.html',context)


def jurnal(request):
	post = Post.objects.filter(category='jurnal')
	context={
	'judul':'blog',
	'heading':'selamat datang',
	'posts':post
	}

	return render(request,'index.html',context)


def tutorial(request):
	post = Post.objects.filter(category='tutorial')
	context={
	'judul':'blog',
	'heading':'selamat datang',
	'posts':post
	}

	return render(request,'index.html',context)