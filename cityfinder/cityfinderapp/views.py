from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *
import numpy as np
import pandas as pd

proper_names = {'cost': 'Cost of Living',
                'walk': "Walkability",
                "bike": 'Bikability',
                "transit": 'Public Transit',
                "safe": 'Safety',
                "community": 'Community',
                "weather": 'Weather'}


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

  #Added here for going back to beginning
  request.session.flush()

  request.session.set_test_cookie()
  if request.session.test_cookie_worked():
    request.session.delete_test_cookie()
  else:
    return HttpResponse("Please enable cookies and try again.")
  
  # this enables us to show any previous selections if user went back to page

  if request.session and 'priorities' in request.session:
    previous_priorities = []
    priorities = [str(p) for p in request.session['priorities']['priorities'].split(',')]
    for priority in priorities:
        previous_priorities.append(proper_names[priority])
    return render(request, 'priorities.html', {'previous_priorities': previous_priorities})

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

def city_results(request):

  request.session['preferences_community'] = request.POST

  #first get user input from sessions and turn into a dict
  print "priorites raw", request.session['priorities']
  print "city size raw", request.session["preferences_citysize"]
  print "weather raw", request.session["preferences_weather"]
  print "community raw", request.session['preferences_community']

  priorities = priorities = [str(p) for p in request.session['priorities']['priorities'].split(',')]

  print "PRIORITIES", priorities

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

  if "community" in priorities:
    query_dict.update(community_preferences)

  if "weather" in priorities:
    query_dict.update(weather_preferences)

  query_dict['priorities'] = priorities
  query_dict.update(citysize_preference)

  print "QUERY DICTIONARY", query_dict


  #delete sessions ## NOTE (Anna Hazard) I am disabling this for my own purposes for now because I need to refresh a lot for the viz
  #request.session.flush()

  #now pass in QUERY DICT TO ALDEN'S WORK
  #then render in results page
  #example to pass in to results to show city data
  #need to call here a func algorithm // Alden
  #walk_city = Walk.objects.order_by('-city')[:50]


  ##### Experimental Data Block for Data Viz. Dummy Data for now, but data should be formated like so before it is rendered ######

  labels = ["city", "match_score", "fall_temp", "winter_temp", "spring_temp", "summer_temp", "bike_score", "transit_score", "walk_score", "rank"]
  headers = ["city_1", "city_2", "city_3", "city_4", "city_5", "city_6", "city_7", "city_8", "city_9", "city_10"]
  
  sample_data = [["New York", "Minneapolis", "Chicago", "Seattle", "Miami", "Austin", "Dallas", "San Francisco", "San Diego", "Salt Lake City"],\
  [.98, .76, .74, .53, .32, .31, .30, .25, .20, .10],\
  [12, 65, 78, 32, 65, 78, 98, 90, 12, 65],\
  [12, 65, 78, 32, 12, 65, 78, 32, 12, 65],\
  [78, 32, 12, 65, 78, 32, 12, 65, 78, 32],\
  [80, 89, 70, 67, 47, 89, 90, 50, 70, 77],\
  [80, 89, 70, 67, 47, 89, 90, 50, 70, 77],\
  [78, 32, 12, 65, 78, 32, 12, 65, 78, 32],\
  [12, 65, 78, 32, 65, 78, 98, 90, 12, 65],\
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
  
  np.array(sample_data)
  
  results = pd.DataFrame(sample_data, index = labels, columns = headers)

  results_json = results.to_json()

  results_csv = results.to_csv()

  ##### End Experimental Block ########

  return render(request, 'city_results.html', {'results': results_json})
