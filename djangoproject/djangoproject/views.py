from django.shortcuts import render

def index(request):
	context={
		'judul':'Home page',
		'content':'ini adalah page dari website ini',

	}

	return render(request,'index.html',context)