from django.shortcuts import render

def index(request):
	context={# harus sejajar di bawah index
			'judulatas':'Uruklangit',
			'subjudul':'Tutorial Django',
			'selamatdatang':'Selamat Datang di Home',
			'app_css':'css/style3.css',
			'banner':'img/banner_home.png',#variabel banner di index html 
			'nav':[
				['about','about'],
				['blog/','blog']
			]

		}

	return render(request,'index.html',context)