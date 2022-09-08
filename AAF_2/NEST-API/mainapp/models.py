from django.db import models

# Create your models here.
class Enquiry(models.Model):

	parentName=models.CharField(max_length=50)
	password=models.CharField(max_length=50)

	income=models.CharField(max_length=50)
	transactions=models.CharField(max_length=50)
	equity=models.CharField(max_length=50)


	def __str__(self):
		return self.userName

