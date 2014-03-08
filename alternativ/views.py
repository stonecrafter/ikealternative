from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from alternativ.models import Item
# VIEWS: return an HttpResponse... or raise Http404 if invalid request.

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'types': {'ARM CHAIR': '01', 
        		  'COUCH': '02', 
        		  'COFFEE TABLE': '03', 
        		  'DESK': '04', 
        		  'BED': '05',
        		  'DINING TABLE': '06', 
        		  'DINING CHAIR': '07', 
        		  'SHELVING': '08'},
    })
    return HttpResponse(template.render(context))

def detail(request, item_type):
	template = loader.get_template('type.html')
	# get ikea item
	ikea_item = Item.objects.filter(store_name="IKEA", item_type__iexact="%s" % item_type)
	# get 4 alternative items
	alt = Item.objects.filter(store_name!="IKEA", item_type__iexact="%s" % item_type)[:4]
	context = RequestContext(request, {
		'ikea_item': ikea_item,
		'alt_items': alt
		})
	return HttpResponse(template.render(context))
	#return HttpResponse("You're looking at category: %s." % item_type)

def options(request, item_type, item_name):
    return HttpResponse("Category: %s. ~~ Alternativ furniture item: %s" % (item_type, item_name))