from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *
import numpy as np
import pandas as pd
import algorithm as algo
import decimal


# ORIGINAL CODE
proper_names = {'cost': 'Cost of Living',
                'walk': "Walkability",
                "bike": 'Bikability',
                "transit": 'Public Transit',
                "safe": 'Safety',
                "community": 'Community',
                "weather": 'Weather'}


def process_slider_input(post):
  '''
  Given a list from JS like so ["sun", 2, "temp", 0]
  Change to dict like so {"sun" : 2, "temp" : 0}
  '''
  attribute_dict = {}
  post = post.items()[1]
  attribute_list = str(post[1]).split(",")

  #FOR WHEN USER PUTS ALL AS INDIFFERENT
  if len(attribute_list) <2:
    return []

  for i, item in enumerate(attribute_list):
    if i%2 == 0:
      key = attribute_list[i]
      score = int(attribute_list[i+1])
      attribute_dict[key] = score

  return attribute_dict

# END OF ORIGINAL CODE
# MODIFIED CODE - followed Django documentation

def priorities(request):
  '''
  View function for the priorities page. User required to have cookies on.
  '''

  request.session.flush()

  request.session.set_test_cookie()
  if request.session.test_cookie_worked():
    request.session.delete_test_cookie()
  else:
    return HttpResponse("Please enable cookies and try again.")
  
  return render(request, 'priorities.html')

def preferences_citysize(request):
  '''
  View function for city size page.
  '''

  request.session['priorities'] = request.POST

  return render(request, 'preferences_citysize.html')

def preferences_weather(request):
  '''
  View function for weather selections page.
  '''
  request.session['preferences_citysize'] = request.POST

  return render(request, 'preferences_weather.html')

def preferences_community(request):
  '''
  View function for communities selection page.
  '''
  request.session['preferences_weather'] = request.POST

  return render(request, 'preferences_community.html')

def error(request):
  '''
  Page displayed in case user preferences do not yield useful results.
  error_message displayed on page. Message varies by error type.
  '''
  return render(request, 'error.html')

def city_results(request):
  '''
  View function for results page. This function builds a query 
  dictionary according to user preferences saved in sessions. 
  Once query dict is built, it is passed to the algorithm, which
  returns a list of candidate cities to render.
  '''
  misstep_messages = ['''Voila! Here are the top cities for you, in order 
  of how well they match your preferences.''']

  request.session['preferences_community'] = request.POST

  #first get user input from sessions and turn into a dict
  priorities = [str(p) for p in request.session['priorities']['priorities'].split(',')]
  communities = [str(p) for p in request.session['preferences_community']['preferences'].split(',')]

  #city size preference to dictionary
  citysize_preference = process_slider_input(request.session["preferences_citysize"])

  #weather preferences to dictionary
  weather_preferences = process_slider_input(request.session["preferences_weather"])

  #check validity of input and redirect to error if invalid
  if priorities == ['']:
    error_message = "It looks like you didn't include any priorities! Make sure you drag some \
    priorities into your list on the first page!"
    return render(request, "error.html", {"error_message" : error_message})

  if weather_preferences and "weather" not in priorities:
    misstep_messages.append("It looks like you expressed some preferences \
      about what kind of weather you like, but didn't include weather in your \
      list of priorities. If you'd like your weather preferences to be \
      considered in your results, include weather in your priorities list \
      next time.")

  if communities != [''] and "community" not in priorities:
    misstep_messages.append("It looks like you expressed some preferences \
      about what kind of communities matter to you, but didn't include community in your \
      list of priorities. If you'd like your community preferences to be \
      considered in your results, include community in your priorities list \
      next time.")

  #building query dict
  query_dict = {}
  if "weather" in priorities:
    if weather_preferences:
      query_dict.update(weather_preferences)
    else:
      misstep_messages.append("It looks like you listed weather as a priority, but didn't specify what \
      kind of weather you like, so your weather preference was not taken into account. \
      If you want to include weather as a priority, specify your weather preferences \
      on the weather page next time.")
      priorities.remove("weather")

  if "community" in priorities:
    if communities != ['']:
      query_dict['communities'] = communities
    else:
      misstep_messages.append("It looks like you listed community as a priority, but didn't specify which \
      communities are important to you, so your community preference was not taken into account. \
      If you want to include community as a priority, specify which communities you care about \
      on the last page next time.")
      priorities.remove("community")

  if citysize_preference:
    query_dict.update(citysize_preference)

  query_dict['priorities'] = priorities

  if len(priorities) == 0:
    error_message = "It looks like you only included weather and/or community in your priorities list, \
    but didn't specify what kind of weather or communities you meant. Be sure to specify your weather and \
    community preferences if you include them in your priorities!"
    return render(request, "error.html", {"error_message" : error_message})  

  city_objects = algo.run_calculations(query_dict)

  cities_list = []
  match_score_list = []

  if len(city_objects) <= 10:
    count = len(city_objects)
  else:
    count = 10

  #check that algorithm returned something
  if len(city_objects) == 0:
    error_message = "It looks like there weren't any cities that matched your \
    preferences. Try again without specifying city size, or with fewer preferences."
    return render(request, "error.html", {"error_message" : error_message})

  for i in range(count):
    #checking for false results list, infinity
    if city_objects[i].score > 100:
      error_message = "It looks like you didn't enter enough preference to \
      get useful results. Try again with more preferences!"
      return render(request, "error.html", {"error_message" : error_message})

    if city_objects[i].score >= 0.001:
      cities_list.append(city_objects[i].name)
      match_score_list.append(round(float('{0:.10f}'.format(city_objects[i].score/100)), 2))

  labels = ["city", "match_score"]
  headers = ["city_1", "city_2", "city_3", "city_4", "city_5", "city_6", "city_7", "city_8", "city_9", "city_10"]
  headers_chopped = headers[:len(cities_list)]

  data = [cities_list, match_score_list]
  np.array(data)
  results = pd.DataFrame(data, index = labels, columns = headers_chopped)
  results_json = results.to_json()

  return render(request, 'city_results.html', {'results': results_json, "missteps": misstep_messages})
