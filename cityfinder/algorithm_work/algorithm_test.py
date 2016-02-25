# CityFinder
# Simple recommendation algorithm
# Limit ten cities
# 2-9-2016

import numpy as np

WEIGHT_DECAY = .15
CITY_DICT = {}

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
    for entry in input_dict:
        if input_dict[entry] is int:
            data[criteria] = [input_dict[entry]]

    for criteria in data: 
        data[criteria].append(get_data(criteria))
        data[criteria][1] = translate_city_names(data[criteria][1])
        data[criteria].append(calculate_z_scores(data[criteria][1][:,1]))

    cities = data[data.keys()[0]][1][:,0]

    return (data, cities)

def get_data(criteria):
    '''
    Gets the city name and relevant column for the criteria passed.

    Input: criteria name
    Output: 2xn array with (city | score_basis)
    '''
    pass

def translate_city_names(array):
    '''
    Takes an array with city names and translates them to a common form.
    '''
    pass

def run_calcuations(input_dict):
    '''
    Carries out algorithm; returns cities dictionary. 

    Input: dictionary from django app
    Output: dictionary mapping city: [overall_score, all_score_array, rank]
    '''
    data, cities = calculate_criteria_scores(input_dict)
    weights = calculate_weights(len(data))
    rv = {}

    for city in cities:
        for criteria in data:
            rv[city] = [None, None, None]
            i = data[criteria][1][:,0].index(city)
            






test1 = {
    walk_score: 1,
    bike_score: 2,
    hispanic: 3,
    size: big
    }

        

