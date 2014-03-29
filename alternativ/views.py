from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from alternativ.models import Item, Store
# VIEWS: return an HttpResponse... or raise Http404 if invalid request.

# Globals
TYPES = {'ARM CHAIR': '01', 
		  'COUCH': '02', 
		  'COFFEE TABLE': '03', 
		  'DESK': '04', 
		  'BED': '05',
		  'DINING TABLE': '06', 
		  'DINING CHAIR': '07', 
		  'SHELVING': '08'
}

STORES = {'CB2': '01',
		   'EQ3': '02',
		   'GAUTIER': '03',
		   'THE BAY': '04',
		   'WEST ELM': '05',
		   'WESTELM': '05',  # kinda hacky, it's OK for now
		   'BO CONCEPT': '06',   # in the interest of deadlines :/
		   'BOCONCEPT': '06'
}

def invalid_url(item, cat=False):
	'''Invalid url handler helper function. Cat is a flag meaning
	the input url to be checked is an item, not a category.'''
	# should be convertable to int
	try:
		num = int(item)
	except ValueError:
		raise Http404
	# should only be two characters long
	if len(item) != 2:
		# that one edge case
		if cat and num == 9:
			return '09'
		else:
			raise Http404
	# there are only 8 categories
	if not cat and num not in range(1,9):
		raise Http404
	# there are only 54 items (yes, this should be changed...)
	if cat and num not in range(9, 55):
		raise Http404

	return item


def about(request):
	template = loader.get_template('about.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'types': TYPES})
	return HttpResponse(template.render(context))


def detail(request, item):
	'''Views handler for the category page - ie. "Couch". '''
	# handle invalid urls
	invalid_url(item)
	template = loader.get_template('type.html')
	# get ikea item
	ikea_item = Item.objects.filter(store_name="IKEA", item_type__iexact="%s" % Item.TYPE_CHOICES[int(item) - 1][1])[0]
	# get all the alternative items
	alt = Item.objects.exclude(store_name="IKEA").filter(item_type__iexact="%s" % Item.TYPE_CHOICES[int(item) - 1][1])
	# create mapping between store name and code
	item_list = {}
	for i in alt:
		item_list[i] = STORES[str(i.store_name.store_name).upper()]
	# pass in the context
	context = RequestContext(request, {
		'item_type': Item.TYPE_CHOICES[int(item) - 1][1],
		'ikea_item': ikea_item.description,
		'subj': ikea_item.subjective_input,
		'alt_items': item_list,
		'code': item
		})
	return HttpResponse(template.render(context))


def options(request, item_type, item):
	# handle invalid urls
	invalid_url(item_type)
	item = invalid_url(item, True)
	# item_type can be used for a back button if desired
	template = loader.get_template('option.html')
	# get the item
	item = Item.objects.get(id=item)
	store = Store.objects.get(store_name=item.store_name)
	# get the corresponding ikea item
	ikea_name = Item.objects.get(id=item_type).item_name.upper()
	# sanity check URL
	correct_type = Item.TYPE_CHOICES[int(item_type) - 1][1].title()
	if item.item_type != correct_type:
		raise Http404
	# get full address for Google Maps display
	full_address = store.store_address + " " + store.city + " " + store.province + " " + store.postal_code
	context = RequestContext(request, {
		# item specific
		'item_code': item,
		'type_code': item_type,
		'item_name': item.item_name,
		'item_desc': item.description,
		'subj': item.subjective_input,
		'price': item.price_multipler,
		'store_name': item.store_name,
		'item_link': item.item_link,
		# ikea item
		'ikea_name': ikea_name,
		# store specific
		'store_code': STORES[str(item.store_name).upper()],
		'store_address': store.store_address,
		'store_website': store.store_website,
		'city': store.city,
		'province': store.province,
		'postal_code': store.postal_code,
		'phone': store.phone_number,
		'full_address': full_address
		})
	return HttpResponse(template.render(context))