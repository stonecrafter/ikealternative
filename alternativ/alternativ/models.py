from django.db import models

# Create your models here.

class IkeaItem(models.Model):
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	opinion = models.TextField()

	def __unicode__(self):   # string representation for debugging
		return self.name

	# here can go custom methods operating on a single tuple, if needed...


class NonIkeaItem(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	opinion = models.TextField()
	store_name = models.CharField(max_length=50)
	store_address = models.CharField(max_length=150)
	store_website = models.URLField()
	ikea_item = models.ForeignKey(IkeaItem, to_field='name')

	def __unicode__(self):   # string representation for debugging
		return self.name