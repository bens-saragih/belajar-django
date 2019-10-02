from django.http import HttpResponse

def index(request):
	return HttpResponse('<h4>home</h4>')


def angka(request,input):
	heading = '<h1>page angka</h1>'
	sera = heading + input# menampilkan hasil dari url angka nya

	return HttpResponse(sera)


def tanggal(request,**input):# input = bebas nama nya apa
	print(input)# nanti nya input dari contoh akan di ambil dan di print di terminal dan menghasilkan dictonary

	# ['tahun'] itu mengambil dari isi input contoh
	# sedangkan input['tahunn'] adalah keyword atau sebagai perantara ke input contoh
	tahun = input['tahun']
	bulan = input['bulan']
	hari = input['hari']
	heading = "<h1>halaman tanggal</h1>"
	datatanggal = "{}/{}/{}".format(tahun,bulan,hari)
	return 	HttpResponse(heading + datatanggal)



def link(request,page):
	str = "<h1>{}</h1>".format(page)

	return HttpResponse(str)

"""
def tanggal(request,tahun,bulan,hari):
	heading = "<h4>Halaman Tanggal</h4>"
	strTahun ="tahun: "+ tahun
	strBulan ="bulan: "+ bulan
	strHari = "hari: "+ hari

	str = heading + strTahun + "</br>" + strBulan +"<br>" + strHari

	return HttpResponse(str)
"""