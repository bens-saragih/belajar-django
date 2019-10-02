from django.shortcuts import render

# Create your views here.

def khususPost(request,input):
	context = {
	'judul': input
	}

	return render(request,'blog/index.html',context)


def categoryPost(request):
	context = {
	'judul': 'Halaman category'
	}

	return render(request,'blog/index.html',context)

def singlePost(request):
	context = {
	'judul': 'Halaman Single'
	}

	return render(request,'blog/index.html',context)

def index(request):
	context = {
	'judul': 'Halaman Home Blog'
	}

	return render(request,'blog/index.html',context)