# CityFinder
# Simple recommendation algorithm
# Limit ten cities
# 2-9-2016

import numpy as np

WEIGHT_DECAY = .15

def calculate_weights(n):
    '''
    Calculates a series of weights based of the number of inputted preferences, n. 

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

def calculate_scores(array):
    '''
    Takes an array of values and computes a matching array with scores. 
    '''
    
    rv = []
    for x in array: 
        rv.append(x / np.average(array))
        

