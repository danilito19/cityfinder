from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *

#keep this code for example
#  walk_city = Walk.objects.order_by('-city')[:50]

def preferences(request):
  template = loader.get_template('preferences.html')
  return render(request, 'preferences.html')
  # return HttpResponse(template.render(context, request))

def priorities(request):
  template = loader.get_template('priorities.html')
  # context = {
  #     'test_context': 'hellow!',
  #   }
  # if request.session.test_cookie_worked():
  #   request.session.delete_test_cookie()
  #   return HttpResponse("You're logged in.")
  # else:
  #   return HttpResponse("Please enable cookies and try again.")
  request.session.set_test_cookie()
    
  return HttpResponse(template.render(request))


#each view has to return an httpresponse or exception
'''
func to get kwargs, transform and get data from model objects

getting data:
Walk.objects.get(city='Chicago')
.filter(**kwargs)
.exlucde(**kwargs)
.get().filter()
.filter(something __lt=10)
.filter(city__inexact="Chicago")
.filter(city__icontains="Chicago")

get data from multiple table objects

'''

