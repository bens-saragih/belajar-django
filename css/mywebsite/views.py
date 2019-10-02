from django.shortcuts import render

def index(request):
	contex = {
	'title':'Kelas Terbuka',
	'hadding':'Selamat Datang',
	'subhading':'Di Kelas Terbuka'
	}
	return render(request,'index.html',contex)