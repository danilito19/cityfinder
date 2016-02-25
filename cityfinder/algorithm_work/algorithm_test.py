# CityFinder
# Simple recommendation algorithm
# Limit ten cities
# 2-9-2016

import numpy as np

WEIGHT_DECAY = .15

def calculate_weights(n):
    '''
    Calculates a series of weights based of the number of inputted 
    preferences, n. 

    Input: n
    Output: a list of weights
    '''    
    rv = [100/n] * n
    for i in range(len(rv)):
        for j in range(i + 1, len(rv)):
            to_add = rv[j] * WEIGHT_DECAY
            rv[j] += -to_add
            rv[i] += to_add

    # Account for rounding error
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

def calculate_city_score(input_dict):
    '''
    Calculates the city score based on inputs. 
    '''
    data = {}
    for entry in input_dict:
        if input_dict[entry] is int:
            data[criteria] = [input_dict[entry]]

    for x in criteria: 
        data[criteria].append(get_data(criteria))

    


def get_data(criteria):
    '''
    Gets the city name and relevant column for the criteria passed.

    Input: criteria name
    Output: 2xn array
    '''
    pass


test1 = {
    walk_score: 1,
    bike_score: 2,
    hispanic: 3,
    size: big
    }

        

