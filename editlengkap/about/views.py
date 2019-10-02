from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'About',
		'subjudul':'Uruklangit',
		'banner':'about/img/banner_about.png',
		'app_css':'about/css/style.css',
		'selamatdatang':'Selamat Datang di About',
		'nav':[
			['/','home'],
			['/blog','blog']
		]


	}
	return render(request,'about/index.html',context)