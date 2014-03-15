from django.db import models


class Item(models.Model):
	# items
	TYPE_CHOICES = (
    	('01', 'ARM CHAIR'),
    	('02', 'COUCH'),
    	('03', 'COFFEE TABLE'),
    	('04', 'DESK'),
    	('05', 'BED'),
    	('06', 'DINING TABLE'),
    	('07', 'DINING CHAIR'),
    	('08', 'SHELVING')
	)

	store_name = models.ForeignKey('Store', to_field='store_name')
	item_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	item_name = models.CharField(max_length=50)
	price_multipler = models.IntegerField()
	item_link = models.URLField()
	description = models.TextField()
	subjective_input = models.TextField(blank=True, null=True)

	def __unicode__(self):   # string representation for debugging
		return self.item_name


class Store(models.Model):
	# stores
	TYPE_CHOICES = (
    	('01', 'IKEA'),
    	('02', 'CB2'),
    	('03', 'EQ3'),
    	('04', 'GAUTIER'),
    	('05', 'THE BAY'),
    	('06', 'WEST ELM'),
    	('07', 'BO CONCEPT')
	)
	
	store_name = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)
	store_website = models.URLField()
	store_address = models.CharField(max_length=150)
	city = models.CharField(max_length=30)
	province = models.CharField(max_length=5)
	postal_code = models.CharField(max_length=10)
	phone_number = models.CharField(max_length=20)

	def __unicode__(self):   # string representation for debugging
		return self.store_name