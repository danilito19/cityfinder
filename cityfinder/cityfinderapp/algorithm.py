# CityFinder
# Recommendation algorithm

import math
import random
import numpy as np
import pandas as pd
import City as city
from .models import *

## ORIGINAL CODE

# Hard coded globals for our implementation
WEIGHT_DECAY = .15
SPECIAL_CRITERIA = ['weather', 'community']
CALCULATED_SCORES = ['safe', 'lgbtq', 'hisp', 'weather', 'community', 'cost']
RELATION_DICT = { 
'cost': [COL, 'total_index'], 
'safe':[Crime, 'bulglary'], 
'community': {'hispanic': [Hisp, 'hisp_count'], 
 'lgbtq': [LGBT, 'Male_Male_HH', 'Female_Female_HH', 'Total_HH'],
 'young': [Age, 'median_age'], 
 'old': [Age, 'old_age_depend_ratio']},
'rent': [Rent, 'bed_1_med_price'], 
'transit': [Walk, 'transit_score'], 
'walk': [Walk, 'walk_score'],  
'bike': [Walk, 'bike_score'], 
'weather': {'sun': [Weather, 'avg_annual_precip_in_days'], 
 'temp': [Weather, 'avg_temp_jan'],
 'seasons' : [Weather, 'avg_temp_jan', 'avg_temp_april', 
    'avg_temp_july', 'avg_temp_oct']},
'cities' : [City, 'city', 'state'], 
'size': [Walk, 'population']}
CATEGORIES = {'seasons': ([0, 10, 20, float('inf')], [0, 1, 2]), 
              'sun': ([0, 75, 125, float('inf')], [0, 1, 2]),
              'temp': ([0, 40, 50, float('inf')], [2, 1, 0]), 
              'size': ([0, 299999, 999999, float('inf')],[0, 1, 2])}

def run_calculations(input_dict):
    '''
    Carries out algorithm; returns list of ranked cities. 

    Input: dictionary from django app
    Output: list of ranked city objects 
    '''
    # Construct the full dataframe of necessary data
    data, priorities, communities, weather, size = construct_dataframe(
        input_dict)
    # If no preferences are selected by user, no calculations are done
    if len(priorities) == 0:
        return []
    # Re-code weather and size to be categorical using CATEGORIES global
    data = add_categorical_information(data, weather, priorities)
    # Do any calculations necessary (rates, agreement, renaming)
    data = calculate_rates(data, weather, communities, priorities)
    # Create a list of City objects for each city in the dataset
    city_data = add_criteria_scores(data, priorities, weather, size, 
        communities)
    # Calculate the weights for each score
    weights = calculate_weights(len(priorities))
    # Use the weights to calculate each City object's score, then rank
    ranked_list = calculate_rank(city_data, weights, priorities)  
    # Take scores and make them 0-100 for readability  
    rv = make_scores_100(ranked_list)
    return rv

def calculate_weights(n):
    '''
    Calculates a series of weights based of the number of inputted 
    preferences, n. N^2 time. 

    Input: n
    Output: a list of weights
    '''    
    # Initialize at equal distribution
    rv = [100/n] * n
    # For each bin, grab a portion of all subsequent bins' size and add to bin
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
    matching a single entry, i, where i in the index in the array.

    Input: array of values
    Output: array or scores OR score for single index
    '''
    rv = []
    # Replace any missing data with average score
    for j in range(len(array)): 
        if np.isnan(array[j]):
            array[j] = np.average(array[~np.isnan(array)])
    # Calculate individual z-score for each city in array
    for x in array: 
        rv.append((x - np.average(array)) / np.std(array))
    # Return an individual city score if requested
    if i != None: 
        return rv[i]
    else:
        return rv

def construct_dataframe(input_dict):
    '''
    Creates data dictionary with all necessary data. Uses RELATION_DICT 
    global to pull data from the django database models. 

    Input: input dictionary
    Output: 
     - pandas dataframe
     - priorities list (in order, highest to lowest)
     - communities list; if not present, None
     - weather dictionary, if not present, None
     - size dictionary
    '''
    data = {}
    # Build priorities, weather, communities, size
    priorities = input_dict['priorities']
    weather = {k:v for (k,v) in input_dict.items() if 'pr' not in k}
    if 'size' in weather:
        size = weather.pop('size')
    else: 
        size = None
    if 'communities' in weather:
        # If user does not select comm prefs, community score not calculated
        communities = weather.pop('communities')
        if len(communities) == 1 and 'community' in priorities:
            priorities.remove('community')
    else:
        communities = []
    if len(weather) == 0 and 'weather' in priorities:
        # If user does not select weather prefs, weather score not calculated
        priorities.remove('weather')

    # Get all the data and stick it into a dictionary
    for criteria in priorities:
        if criteria not in SPECIAL_CRITERIA:
            criteria_info = RELATION_DICT[criteria]
            data[criteria] = get_data(criteria_info)
        elif criteria in SPECIAL_CRITERIA:
            for key in RELATION_DICT[criteria]:
                if criteria is 'weather':
                    criteria_info = RELATION_DICT[criteria][key]
                    data[key] = get_data(criteria_info)
                else: 
                    criteria_info = RELATION_DICT[criteria][key]
                    data[key] = get_data(criteria_info)                    
    data['size'] = get_data(RELATION_DICT['size'])
    data['cities'] = get_data(RELATION_DICT['cities'])
    # Merge all the data contained in the the data dictionary
    rv = data['cities']
    rv.columns = ['city', 'city_id', 'state']
    for key in data:
        if key != 'cities':
            rv = pd.merge(rv, data[key], on='city_id')

    return (rv, priorities, communities, weather, size)

def get_data(criteria_info):
    '''
    Gets the city name and relevant column(s) for the criteria passed.

    Input: criteria name
    Output: pandas dataframe
    '''
    # Specific query information for cities because of db inconsistencies
    if criteria_info == RELATION_DICT['cities']:
        data = []
        for col in criteria_info[1:]:
            pull = criteria_info[0].objects.values('id', col)
            data.append(pull)
        rv = pd.DataFrame.from_records(data[0])
        for df in data[1:]:
            df = pd.DataFrame.from_records(df)
            rv = pd.merge(rv, df, on='id')
        return rv

    # All other queries
    else:
        data = []
        for col in criteria_info[1:]:
            data.append(criteria_info[0].objects.values('city_id', col))
        rv = pd.DataFrame.from_records(data[0])
        for df in data[1:]:
            df = pd.DataFrame.from_records(df)
            rv = pd.merge(rv, df, on='city_id')
        return rv

def add_categorical_information(data, weather, priorities):
    '''
    Converts several columns into categorical information for filtering
    purposes. Uses information in CATEGORIES global for naming.

    Input: pandas dataframe, weather dictionary, priorities list
    Output: pandas dataframe with categorical data added
    '''
    # Convert weather attributes to categorical data
    if 'weather' in priorities:
        for key in weather: 
            if key == 'seasons':
                cols = []
                concat = []
                # Get all temperature column names from data
                for x in data.columns:
                    if 'avg_temp' in x: 
                        cols.append(x)
                # Remove extra temp cols due to concatentation in data build
                if len(cols) > 4: 
                    cols.remove('avg_temp_jan_y')    
                # Get data corresponding to columns & concatenate
                for col in cols: 
                    concat.append(data[col])
                temps = pd.concat(concat, axis = 1)
                # New calculated columns
                temps['temp_variation'] = temps.var(axis = 1)
                temps['temp_sd'] = temps['temp_variation'].apply(math.sqrt)
                temps['seasons'] = pd.cut(temps['temp_variation'], 
                    CATEGORIES[key][0], labels = CATEGORIES[key][1], 
                    right = True)
                # Add only seasons to dataset
                temps = temps['seasons']
                data = pd.concat([data, temps], axis = 1)
            elif key == 'sun':
                data['sun'] = pd.cut(data['avg_annual_precip_in_days'],  
                 CATEGORIES[key][0], labels = CATEGORIES[key][1], right = True)
            elif key == 'temp':
                # Get Jan temps; structured in case there are extra Jan cols
                for x in data.columns: 
                    if 'avg_temp_jan' in x: 
                        col = x
                        break
                temp_level = pd.cut(data[col], CATEGORIES[key][0],
                  labels = CATEGORIES[key][1], right = True)
                temp_level.name = 'temp'
                data = pd.concat([data, temp_level], axis = 1)

    # Convert size to categorical
    data['size'] = pd.cut(data['population'], CATEGORIES['size'][0], labels = 
        CATEGORIES['size'][1], right = True)
    return data

def calculate_rates(data, weather, communities, priorities):
    '''
    Calculates safety (burglaries per 1000 residents), hispanic (hispanic 
    individuals per 1000 residents), and lgbtq rates (LGBT HH per 1000 
    individuals). Renames old age dependency to old. Flips age cardinality so 
    that younger median age is a higher score. Flips CPI cardinality.

    Input: pandas dataframe, weather dictionary, communities list, priorities
    list
    Output: pandas dataframe with new columns for needed calculations
    '''
    # Runs necessary transformation if user preferences require it
    if 'safe' in priorities:
        # Inverts score so that lower rates are better
        data['burg_rate'] = data['bulglary'] / (data['population'] / 1000)
        data['safe'] = ((-1 * pd.DataFrame(calculate_z_scores(data['burg_rate'] \
         ))) * np.std(data['burg_rate'])) + np.average(data['burg_rate'])
    if 'hisp' in communities and 'community' in priorities:
        data['hisp'] = data['hisp_count'] / (data['population'] / 1000)
    if 'lgbtq' in communities and 'community' in priorities:
        data['lgbtq'] = (data['Female_Female_HH'] + data['Male_Male_HH']) / \
         (data['population'] / 1000)
    if 'old' in communities and 'community' in priorities:
        data['old'] = data['old_age_depend_ratio']
    if 'young' in communities and 'community' in priorities:
        # Inverts score so that younger median age is a higher score
        data['young'] = ((-1 * pd.DataFrame(calculate_z_scores(data['median_age'] \
         ))) * np.std(data['median_age'])) + np.average(data['median_age'])
    if 'cost' in priorities:
        # Inverts CPI so that lower CPI is a higher score
        data['cost'] = ((-1 * pd.DataFrame(calculate_z_scores(data['total_index'] \
         ))) * np.std(data['total_index'])) + np.average(data['total_index'])
    if 'weather' in priorities:
        data = calculate_weather(data, weather)
    if 'community' in priorities:
        data = calculate_community(data, communities)
    return data

def calculate_weather(data, weather):
    '''
    Calculates weather agreement. If 2/3 weather options agree with the 
    specifications of the user, will return .666 repeating and so on.

    Input: pandas dataframe, weather dictionary
    Output: pandas dataframe with weather column for weather agreement
    '''
    count = 1
    cols = []
    # Pull column of True/False for agreement, convert each to 0/1
    for x in weather:
        col = 'weather_' + str(count)
        data[col] = (data[x] == int(weather[x]))
        data[col] = data[col].astype(int, copy = False)
        count += 1
    # Sum agreements and then divide by total number of columns
    data['weather'] = pd.concat([data['weather_' + str(i)] for i in 
        range(1, count)], axis=1).sum(axis=1) / 3
    return data

def calculate_community(data, communities):
    '''
    Calculates community column average score. If no communities are selected,
    will return the same dataframe without edits. 

    Input: pandas dataframe, communities list
    Output: pandas dataframe with communities agreement for each city.
    '''
    # Find average score for all relevant community columns
    if len(communities) > 1:
        data['community'] = pd.concat([pd.DataFrame(calculate_z_scores(
         data[x])) for x in communities], axis = 1).sum(axis=1) /\
         len(communities)
    # Input gives '' when no communities are selected, adjustment
    elif len(communities) == 1:
        data['community'] = data[communities[0]]
    return data

def add_criteria_scores(data, priorities, weather, size, communities):
    '''
    Creates City objects for each city and adds all criteria scores. 

    Input: list of cities, data dictionary
    Output: city_data list
    '''
    rv = []
    for row in data.iterrows():
        cit = city.City(row[1]['city'], row[1]['state'], row[1]['city_id'], 
            row[1]['size'])
        index = data[data['city_id'] == [row[1]['city_id']]].index[0]
        scores = {}
        for key in priorities:
            # For each priority inputted, calculate the z-scores for this city
            if key not in SPECIAL_CRITERIA and key not in CALCULATED_SCORES:
                scores[key] = [calculate_z_scores(data[RELATION_DICT[key][1]],
                    index)] 
            elif key in CALCULATED_SCORES:
                if key == 'community':
                    scores[key] = [calculate_z_scores(data[key], index)]
                elif key == 'community':
                    # Quirk of data passing; throw in a value
                    scores[key] = [1]
                else: 
                    scores[key] = [calculate_z_scores(data[key], index)]
            # Set NaNs equal to average
            if str(scores[key]) == 'nan':
                scores[key] = [0]

        cit.all_scores = pd.DataFrame.from_dict(scores)

        if size != None:
            if cit.size == int(size):
                rv.append(cit)
        else: 
            rv.append(cit)

    return rv

def calculate_rank(city_data, weights, priorities):
    '''
    Calculates rank from a list of cities with scores.
    '''
    # Create tuple, use list sort
    rv = []
    for entry in city_data:
        entry.calculate_score(weights, priorities)
        rv.append((entry.score, entry))
    rv = sorted(rv, reverse = True)
    # Add rank
    rank = 1
    for i in range(len(rv)): 
        entry = rv.pop(0)
        entry[1].rank = rank
        rank += 1
        rv.append(entry[1])
    return rv

def make_scores_100(ranked_list):
    '''
    Converts the scores from the final ranked_list cities into a 
    scale of 0-100, for comprehension.
    '''
    scores_list = []
    for city in ranked_list:
        scores_list.append(city.score)
    # Calculate current range
    scores = np.array(scores_list)
    if scores.min() < 0:
        max_score = scores.max() - scores.min()
        min_score = 0
    else:
        max_score = scores.max()
        min_score = scores.min()
    # Map old values onto 0-100 range
    for i in range(len(scores_list)):
        if scores.min() < 0:
            ranked_list[i].score = 100 * ((scores_list[i] - scores.min()) / \
            (max_score - min_score))
        else:
            ranked_list[i].score = 100 * (scores_list[i] / \
            (max_score - min_score))
    return ranked_list
