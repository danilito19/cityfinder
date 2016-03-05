# CityFinder
# Simple recommendation algorithm
# Limit 100 cities
# 2-9-2016

import numpy as np
import City as city
## from cityfinderapp.models import *

WEIGHT_DECAY = .15
RELATION_DICT = {'colleges': 'cityfinderapp_academic', 
'age':'cityfinderapp_age', 
'cost':'cityfinderapp_col', 'crime':'cityfinderapp_crime', 
'hisp':'cityfinderapp_hisp', 'lgbt':'cityfinderapp_lgbt', 
'rent':'cityfinderapp_rent', 'transit':'cityfinderapp_walk', 
'walk':'cityfinderapp_walk', 'bike':'cityfinderapp_walk'
'weather':'cityfinderapp_weather' }

def calculate_weights(n):
    '''
    Calculates a series of weights based of the number of inputted 
    preferences, n. N^2 time. 

    Input: n
    Output: a list of weights
    '''    
    rv = [100/n] * n
    for i in range(len(rv)):
        for j in range(i + 1, len(rv)):
            to_add = rv[j] * WEIGHT_DECAY
            rv[j] += -to_add
            rv[i] += to_add

    # Account for rounding error so that sum is 100
    if sum(rv) > 100: 
        sub = 100 - sum(rv)
        rv[-1] += sub     

    return sorted(rv, reverse = True)

def calculate_z_scores(array, i = None):
    '''
    Takes an array of values and computes a matching array with normalized 
    z-scores. Returns either the full array or, optionally, the z-score 
    matching i.

    Input: array of values
    Output: array or scores OR score for single index
    '''
    rv = []
    for x in array: 
        rv.append((x - np.average(array)) / np.std(array))

    if i: 
        return rv[i]
    else:
        return rv

def calculate_criteria_scores(input_dict):
    '''
    Calculates the city score based on inputs; creates data dictionary.

    Input: input dictionary
    Output: 
    - data dictionary mapping criteria: [rank, data_array, score_array]
    - cities list
    '''
    data = {}
    priority = len(input_dict[0])
    
    for criteria in input_dict['priorities']:
        data[criteria] = [get_data[criteria]]
        data[criteria].append(calculate_z_scores(data[criteria][1][:,1]))
        priority += -1

    return data

def get_data(criteria):
    '''
    Gets the city name and relevant column for the criteria passed.

    Input: criteria name
    Output: 2xn array with (city | score_basis)
    '''
    pass

def add_criteria_scores(cities, data):
    '''
    Creates City objects for each city and adds all criteria scores. 

    Input: list of cities, data dictionary
    Output: city_data dictionary mapping city: City object
    '''
    rv = {}
    for i in range(len(cities)):
        rv[cities[i]] = city.City(cities[i][1])
        for criteria in data:
            city = rv[cities[i]].name
            i_array = data[criteria][1] is city
            city_score = data[criteria][1][i_array]
            np.concatenate((rv[i].all_scores, city_score), axis = 1)

def calculate_rank(city_dict):
    '''
    '''
    pass

def run_calculations(input_dict):
    '''
    Carries out algorithm; returns cities dictionary. 

    Input: dictionary from django app
    Output: list of ranked cities, dictionary mapping city: city object, 
    '''
    data = calculate_criteria_scores(input_dict)
    cities = get_data('cities')
    city_data = add_criteria_scores(cities, data)
    weights = calculate_weights(len(data))

    for entry in city_data:
        city_data[entry].calculate_score(weights)

    ranked_list = calculate_rank(city_dict)
    return ranked_list, city_data

test1 = {
    'priorities': ['walk', 'weather'],
    'preferences': {'city' : 1,
                'sun' : 2}
    }

# Output should be a list of Class Object for Cities in order of rank:
#   rank
#   score
#   table of scores

# There is a city name that works across all relations - inside views
# Pull city, col from relation if city is in key relation

# City.objects_all() <- all city names
# Loop through these
#   Loop through preferences
#       grab, store in new class



