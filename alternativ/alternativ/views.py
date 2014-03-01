from django.http import HttpResponse
from django.shortcuts import render
# VIEWS: return an HttpResponse... or raise Http404 if invalid request.

def index(request):
    #return HttpResponse("Hello, world. You're at the home page.")
    context = {}    # things can be passed here
    return render(request, 'index.html', context)

def detail(request, item_type):
    return HttpResponse("You're looking at category: %s." % item_type)

def options(request, item_type, item_name):
    return HttpResponse("Category: %s. ~~ Alternativ furniture item: %s" % (item_type, item_name))