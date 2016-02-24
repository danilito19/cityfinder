from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *

#keep this code for example
#  walk_city = Walk.objects.order_by('-city')[:50]

def priorities(request):
  # All this happens before any HTML is sent to the browser
  request.session.set_test_cookie()
  if request.session.test_cookie_worked():
    request.session.delete_test_cookie()
  else:
    return HttpResponse("Please enable cookies and try again.")
  
  # this enables us to show any previous selections if user went back
  # to the first page. 
  # context = {'previous_priorities': []}
  # if request.session and request.session['priorities']:
  #   for priority in request.session['priorities']:
  #     context['previous_priorities'].append(priority)

  # render HTML for browser here
  return render(request, 'priorities.html')


def preferences(request):
  # we get ordered priorities from revious page via request.POST
  #get them into a kwargs dict to query db

  kwargs = {}
  p = request.POST.items()[1]
  key = str(p[0])
  priorities = str(p[1]).split(',')
  kwargs[key] = priorities
  print kwargs


  # we now save these priorities for later use, or if user goes back
  request.session['priorities'] = kwargs

  # return render(request, 'preferences.html', {'test_context': stored_variable})
  return render(request, 'preferences.html')


def city_results(request):

  #first get priorities list
  kwargs = request.session['priorities'] 
  print 'priority values are:', kwargs

  #now get post from preferences view
  
  print 'these are preferences', request.POST.items()[1]

  #show city list in bootstrap table
  return render(request, 'city_results.html')


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

