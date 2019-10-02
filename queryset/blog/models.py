from django.db import models

# Create your models here.
 
class Post(models.Model):
	#tipe data mysql
	judul = models.CharField(max_length=200)
	body = models.TextField()
	category = models.CharField(max_length=100)
	waktuposting = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return "{}.{}".format(self.id,self.judul)