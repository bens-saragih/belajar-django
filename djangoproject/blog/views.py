from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
	posts = Post.objects.all()
	categories = Post.objects.values("category").distinct();#distinct berguna untuk
	# memfilter category agar yang muncul hanya cukup satu,jika tidak menggunakan itu maka akan keluar category sesuai banyakknya post yang menggunakan category

	context={
		'judul':'Home Blog',
		'content':'Ini adalah halaman home nya blog',
		'Categories':categories,
		'Posts':posts

	}

	return render(request,'blog/index.html',context)

def detailPost(request,slugInput):
	posts = Post.objects.get(slug = slugInput)
	categories = Post.objects.values("category").distinct();

	context={
		'judul':'Home Blog',
		'content':'Ini adalah halaman home nya blog',
		'Categories':categories,
		'Posts':posts

	}

	return render(request,'blog/detail.html',context)


def categoryPost(request,categoryInput):
	posts = Post.objects.filter(category=categoryInput)
	categories = Post.objects.values("category").distinct();

	context={
		'judul':'Home Blog',
		'content':'Ini berdasarkan category',
		'Posts':posts,
		'Categories':categories
		}

	return render(request,'blog/category.html',context)
