from django.db import models

# Create your models here.

class Item(models.Model):

	TYPE_CHOICES = (
    	('AC', 'Arm Chair'),
    	('CO', 'Couch'),
    	('CT', 'Coffee Table'),
    	('DE', 'Desk'),
    	('BE', 'Bed'),
    	('DT', 'Dining Table'),
    	('DC', 'Dining Chair'),
    	('SH', 'Shelving')
	)

	store_name = models.CharField(max_length=50)
	item_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	item_name = models.CharField(max_length=50)
	item_link = models.URLField()
	description = models.TextField()
	subjective_input = models.TextField(blank=True, null=True) # won't be done for MVP
	store_address = models.CharField(max_length=150)
	store_website = models.URLField()
	store_address = models.CharField(max_length=150)

	def __unicode__(self):   # string representation for debugging
		return self.name