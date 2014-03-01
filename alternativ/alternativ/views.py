from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the home page.")

def detail(request, ikea_name):
    return HttpResponse("You're looking at IKEA furniture: %s." % ikea_name)

def options(request, ikea_name, non_ikea_name):
    return HttpResponse("IKEA furniture: %s. ~~ Alternativ furniture: %s" % (ikea_name, non_ikea_name))