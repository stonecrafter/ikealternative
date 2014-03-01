from django.db import models

# Create your models here.

class Ikea_Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	opinion = models.TextField()


class Non_Ikea_Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	opinion = models.TextField()
	store_name = models.CharField(max_length=50)
	store_address = models.CharField(max_length=150)
	store_website = models.URLField()
	ikea_item = models.ForeignKey(Ikea_Item, to_field='name')