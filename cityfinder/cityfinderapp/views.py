from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import *

def home(request):
    walk_city = Walk.objects.order_by('-city')[:50]
    #output = ', '.join([str(q) for q in walk_city])
    return render(request, 'base.html', {'cities': walk_city})

#each view has to return an httpresponse or exception