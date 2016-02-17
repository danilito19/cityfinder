from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import *

def preferences(request):
    walk_city = Walk.objects.order_by('-city')[:50]
    return render(request, 'preferences.html', {'cities': walk_city})

def priorities(requst):
    walk_city = Walk.objects.order_by('-city')[:50]
    return render(request, 'priorities.html', {'cities': walk_city})

#each view has to return an httpresponse or exception