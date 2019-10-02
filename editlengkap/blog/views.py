from django.shortcuts import render

def index(request):
	context = {
		'judul':'Blog',
		'subjudul':'Uruklangit',
		'selamatdatang':'Selamat Datang di Blog',
		'daftar':'Register',
		'app_css':'blog/css/style.css',
		'bebas_regis':'blog/tes/style.css',
		'banner':'blog/img/banner_blog.png',# cara lain, dan template global yg dipakai
		'nav':[
			['/','home'],
			['/about','about']
		]	
	}
	return render(request,'blog/index.html',context)#menggunakan template global
