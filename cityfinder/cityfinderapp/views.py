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
  # to the first page. Otherwise no harm done
  context = {'previous_priorities': []}
  if request.session['priorities']:
    for priority in request.session['priorities']:
      context['previous_priorities'].append(priority)

  # render HTML for browser here
  return render(request, 'priorities.html', context)


def preferences(request):
  # we get priorities from previous page via request.POST
  print request.POST
  # we now save these priorities for later use, or if user goes back
  request.session['priorities'] = request.POST['priorities']
  # stored_variable = request.session['test']
  # return render(request, 'preferences.html', {'test_context': stored_variable})
  return render(request, 'preferences.html')




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

