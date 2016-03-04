from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *



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

  return render(request, 'priorities.html')

def transform_post_to_dict(post):
  '''
  Given a post item, transform values into a dict
  '''

  d = {}
  post = post.items()[1]
  key = str(post[0])
  values = str(post[1]).split(',')

  d[key] = values

  return d 


def preferences(request):
  # we get ordered priorities from revious page via request.POST
  # we now save these priorities for later use, or if user goes back
  request.session['priorities'] = request.POST

  return render(request, 'preferences.html')

def preferences_citysize(request):

  request.session['preferences'] = request.POST
  return render(request, 'preferences_citysize.html')

def preferences_weather(request):
  request.session['preferences_citysize'] = request.POST

  return render(request, 'preferences_weather.html')

def preferences_community(request):
  request.session['preferences_weather'] = request.POST

  return render(request, 'preferences_community.html')

def city_results(request):

  request.session['preferences_community'] = request.POST

  #first get user input from sessions and turn into a dict

  print request.session['priorities']
  print request.session['preferences_community'] 
  # priorities = transform_post_to_dict(request.session['priorities'])
  # preferences = transform_post_to_dict(request.session['preferences'])
  # preferences_citysize = transform_post_to_dict(request.session['preferences_citysize'])
  # preferences_weather = transform_post_to_dict(request.session['preferences_weather'])
  # preferences_community = transform_post_to_dict(request.session['preferences_community'])

  # print priorities
  # print preferences
  # print preferences_citysize
  # print preferences_weather
  # print preferences_community

  #example to pass in to results to show city data
  #need to call here a func algorithm // Alden
  walk_city = Walk.objects.order_by('-city')[:50]

  return render(request, 'city_results.html', {'results': walk_city})


#each view has to return an httpresponse or exception
'''
func to get kwargs, transform and get data from model objects

#keep this code for example
#  walk_city = Walk.objects.order_by('-city')[:50]


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

