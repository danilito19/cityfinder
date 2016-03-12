import os
import csv
import django


## ORIGINAL CODE

os.environ["DJANGO_SETTINGS_MODULE"] = "cityfinder.settings"
django.setup()
from cityfinderapp.models import *

d = '~/Dropbox/city-data/'

def to_float(val, null_value):
    '''
    Transform a val to a float, else use null_value
    '''
    return float(val) if val != null_value else None    

def transform_walk(line):
    '''
    Transform the walk score data to use django models.
    '''
    result = {}
    result["state"] = line[1]
    result["walk_score"] = to_float(line[2], '')
    result["transit_score"] = to_float(line[3], '')
    result["bike_score"] = to_float(line[4], '')
    result["population"] = to_float(line[5], '')

    return result

def transform_weather(line):
    '''
    Transform the weather data to use django models.
    '''

    result = {}
    
    result["state"] = line[1]
    result["avg_temp_jan"] = to_float(line[2], 'trace')
    result["avg_temp_april"] = to_float(line[3], 'trace')
    result["avg_temp_july"] = to_float(line[4], 'trace')
    result["avg_temp_oct"] = to_float(line[5], 'trace')
    result["avg_annual_precip_in"] = to_float(line[6], 'trace')
    result["avg_annual_precip_in_days"] = to_float(line[7], 'trace')
    result["avg_annual_precip_snowfall"] = to_float(line[8], 'trace')

    return result

def transform_rents(line):
    '''
    Transform the rents data to use django models.
    '''
    result = {}

    result["state"]=line[1]
    result["bed_1_med_price"]=to_float(line[2], '')
    result["bed_2_med_price"]=to_float(line[3], '')

    return result

def transform_crime(line):
    '''
    Transform the crime data to use django models.
    '''
    result = {}

    result["state"]=line[1]
    result["population"]=to_float(line[2], '')
    result["violent_crime"]=to_float(line[3], '')
    result["murder"]=to_float(line[4], '')
    result["rape"]=to_float(line[5], '')
    result["robbery"]=to_float(line[6], '')
    result["aggrev_assault"]=to_float(line[7], '')
    result["property_crime"]=to_float(line[8], '')
    result["bulglary"]=to_float(line[9], '')
    result["larceny_theft"]=to_float(line[10], '')
    result["car_theft"]=to_float(line[11], '')
    result["arson"]=to_float(line[12], '')

    return result

def transform_COL(line):
    '''
    Transform the cost of living data to use django models.
    '''
    result = {}

    result["state"]=line[1]
    result["total_index"]=to_float(line[2], '')
    result["grocery"]=to_float(line[3], '')
    result["housing"]=to_float(line[4], '')
    result["utilities"]=to_float(line[5], '')
    result["transport"]=to_float(line[6], '')
    result["health"]=to_float(line[7], '')
    result["misc"]=to_float(line[8], '')

    return result

def transform_LGBT(line):
    '''
    Transform the lgbt data to use django models.
    '''

    result = {}

    result["state"]=line[1]
    result["Total_HH"]=to_float(line[2], '')
    result["THH_MOE"]=to_float(line[3], '')
    result["Total_Unmarried"]=to_float(line[4], '')
    result["TU_MOE"]=to_float(line[5], '')
    result["Male_Male_HH"]=to_float(line[6], '')
    result["MMHH_MOE"]=to_float(line[7], '')
    result["Female_Female_HH"]=to_float(line[8], '')
    result["FFHH_MOE"]=to_float(line[9], '')
    result["All_Other_HH"]=to_float(line[10], '')
    result["AOH_MOE"]=to_float(line[11], '')

    return result

def transform_hisp(line):
    '''
    Transform the hispanic population data to use django models.
    '''

    result = {}

    result["state"]=line[1]
    result["hisp_count"]=to_float(line[2], '')
    result["hisp_MOE"]=to_float(line[3], '')

    return result

def transform_ages(line):
    '''
    Transform the age data to use django models.
    '''

    result = {}

    result["state"]=line[1]
    result["population"]=to_float(line[2], '')
    result["median_age"]=to_float(line[3], '')
    result["age_depend_ratio"]=to_float(line[4], '')
    result["old_age_depend_ratio"]=to_float(line[5], '')
    result["child_depend_ratio"]=to_float(line[6], '')

    return result

def import_data(model, file_name, func):
    '''
    Import data from csv and adds data to the appropriate model by relating
    it to a city id if the city in the data matches by city name and state.
    '''

    path = os.path.expanduser(d + file_name)

    with open(path) as f:
        data = csv.reader(f, delimiter=',')
        count = 0
        next(data)
        for line in data:
            print('lINE 0, LINE 1'), line[0], line[1]
            city = City.objects.filter(city__icontains=line[0], state__icontains=line[1])
            if city:
                print('Found city', city)
                ob = model(city=city[0], **func(line))
                ob.save()


if __name__=="__main__":

    info = {Walk: ('walk-transit-bike-score.csv', transform_walk),
            Weather: ('weather-cities.csv', transform_weather),
            Rent: ('MedianRents.csv', transform_rents),
            Crime: ('crime_2014.csv', transform_crime),
            COL: ('COLindex.csv', transform_COL),
            LGBT: ('LGBT_households.csv', transform_LGBT),
            Hisp: ('hisp.csv', transform_hisp),
            Age: ('ages.csv', transform_ages)}

    for key, val in info:
        import_data(key, val[0], val[1])

