from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *



def process_user_list(post):
  '''
  Given a post item, transform strings into a dict
  with a list of priorities or preferences.
  '''

  attribute_dict = {}
  post = post.items()[1]
  key = str(post[0])
  values = str(post[1]).split(',')

  attribute_dict[key] = values

  return attribute_dict

def process_slider_input(post):
  '''
  Given a list from JS like so ["sun", 2, "temp", 0]
  Change to dict like so {"sun" : 2, "temp" : 0}
  '''
  attribute_dict = {}
  post = post.items()[1]
  attribute_list = str(post[1]).split(",")

  for i, item in enumerate(attribute_list):
    if i%2 == 0:
      key = attribute_list[i]
      score = int(attribute_list[i+1])
      attribute_dict[key] = score

  return attribute_dict

def priorities(request):
  # All this happens before any HTML is sent to the browser
  request.session.set_test_cookie()
  if request.session.test_cookie_worked():
    request.session.delete_test_cookie()
  else:
    return HttpResponse("Please enable cookies and try again.")
  
  # this enables us to show any previous selections if user went back
  #to the first page. 
  # context = {'previous_priorities': []}
  # if request.session and request.session['priorities']:
  #   for priority in request.session['priorities']:
  #     context['previous_priorities'].append(priority)

  return render(request, 'priorities.html')

def preferences_citysize(request):
  request.session['priorities'] = request.POST
  return render(request, 'preferences_citysize.html')

def preferences_weather(request):
  request.session['preferences_citysize'] = request.POST

  return render(request, 'preferences_weather.html')

def preferences_community(request):
  request.session['preferences_weather'] = request.POST

  return render(request, 'preferences_community.html')

def city_results_experimental(request):
  cities = ["New York", "Minneapolis", "Chicago", "Seattle", "Miami", "Austin", "Dallas", "San Francisco", "San Diego", "Salt Lake City"]
  match_scores = [98, 76, 74, 53, 32, 31, 30, 25, 20, 10, 5]
  fall_temp = [12, 65, 78, 32, 65, 78, 98, 90, 12, 65]
  winter_temp = [12, 65, 78, 32, 12, 65, 78, 32, 12, 65]
  spring_temp = [78, 32, 12, 65, 78, 32, 12, 65, 78, 32]
  summer_temp = [80, 89, 70, 67, 47, 89, 90, 50, 70, 77]
  bike_score = [80, 89, 70, 67, 47, 89, 90, 50, 70, 77]
  transit_score = [78, 32, 12, 65, 78, 32, 12, 65, 78, 32]
  walk_score = [12, 65, 78, 32, 65, 78, 98, 90, 12, 65]

  return render(request, 'city_results_experimental.html', {"cities": cities})

def city_results(request):

  request.session['preferences_community'] = request.POST

  #first get user input from sessions and turn into a dict
  print "priorites raw", request.session['priorities']
  print "city size raw", request.session["preferences_citysize"]
  print "weather raw", request.session["preferences_weather"]
  print "community raw", request.session['preferences_community']

  priorities = process_user_list(request.session["priorities"])
  print "priorites", priorities

  #city size preference to dictionary
  citysize_preference = process_slider_input(request.session["preferences_citysize"])
  print "city size prefs", citysize_preference

  #weather preferences to dictionary
  weather_preferences = process_slider_input(request.session["preferences_weather"])
  print "weather prefs", weather_preferences

  #community preferences to dictionary
  community_preferences = process_user_list(request.session["preferences_community"])
  print "comm prefs", community_preferences

  #building query dict
  query_dict = {}

  if "community" in priorities["priorities"]:
    query_dict.update(community_preferences)

  if "weather" in priorities["priorities"]:
    query_dict.update(weather_preferences)

  query_dict.update(priorities)
  query_dict.update(citysize_preference)

  print "QUERY DICTIONARY", query_dict


  #now pass in QUERY DICT TO ALDEN'S WORK
  #then render in results page
  #example to pass in to results to show city data
  #need to call here a func algorithm // Alden
  walk_city = Walk.objects.order_by('-city')[:50]

  return render(request, 'city_results.html', {'results': walk_city})
