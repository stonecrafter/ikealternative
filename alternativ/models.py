from django.db import models


# the actual items model to store
class Item(models.Model):

	TYPE_CHOICES = (
    	(1, 'Arm Chair'),
    	(2, 'Couch'),
    	(3, 'Coffee Table'),
    	(4, 'Desk'),
    	(5, 'Bed'),
    	(6, 'Dining Table'),
    	(7, 'Dining Chair'),
    	(8, 'Shelving')
	)

	id = models.IntegerField(primary_key=True)
	store_name = models.CharField(max_length=50)
	store_id = models.IntegerField()
	item_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	item_name = models.CharField(max_length=50)
	item_link = models.URLField()
	description = models.TextField()
	subjective_input = models.TextField(blank=True, null=True) # won't be done for MVP
	store_website = models.URLField()
	store_address = models.CharField(max_length=150)
	city = models.CharField(max_length=30)
	province = models.CharField(max_length=5)
	postal_code = models.CharField(max_length=10)
	phone_number = models.CharField(max_length=20)

	def __unicode__(self):   # string representation for debugging
		return self.item_name