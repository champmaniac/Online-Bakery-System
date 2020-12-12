from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.db.models.functions import Now



# Create your models here.


class ExpiredManager(models.Manager):

	def get_queryset(self):
		return super().get_queryset().annotate(
			expired=ExpressionWrapper(Q(mfg_date__lt=Now()), output_field=BooleanField())
		)


def fourteen_days_hence():
	return timezone.now() + timezone.timedelta(days=14)


class Inventory(models.Model):
	product_id = models.AutoField
	name = models.CharField(max_length =200, null = True)
	category = models.CharField(max_length=50, default="")
	subcategory = models.CharField(max_length=50, default="")
	desc = models.CharField(max_length =300)
	qty = models.IntegerField(default=10)
	mfg_date = models.DateField(default=timezone.now)
	exp_date = models.DateField(default=fourteen_days_hence)


	objects = ExpiredManager()
	price = models.DecimalField(max_digits= 7, decimal_places= 2)
	digital =models.BooleanField(default= False, null =True, blank=True)
	image = models.ImageField(upload_to='shop/images',default ="")
	


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Inventory"



	

class Contact(models.Model):
	msg_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=70, default="")
	phone = models.CharField(max_length=70, default="")
	desc = models.CharField(max_length=500, default="")


	def __str__(self):
		return self.name



class Sale(models.Model):
	date= models.DateField(default= timezone.now)
	order_id = models.AutoField(primary_key=True)
	items_json = models.CharField(max_length=5000)
	name = models.CharField(max_length=90)
	email = models.CharField(max_length=111)
	address = models.CharField(max_length=111)
	city = models.CharField(max_length=111)
	state = models.CharField(max_length=111)
	zip_code = models.CharField(max_length=111)
	phone = models.CharField(max_length=111, default="")
	total= models.CharField(max_length=10,default="")



class Report(models.Model):
	date= models.DateField(default= timezone.now)





	class Meta:
		verbose_name_plural = "Report"


# Create your models here.
