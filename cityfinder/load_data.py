from django.db import connections
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist    
from cityfinderapp import models

'''
Inspired by: 
http://jantoniomartin.tumblr.com/post/15233766067/django-how-to-import-data-from-an-external
'''

def setup_cursor():
    try:
        return connections['default'].cursor()
    except ConnectionDoesNotExist:
        print "Legacy database is not configured"
        return

def import_walk():
    cursor = setup_cursor()
    if cursor is None:
        print('no cursor')
        return
    sql = """SELECT * FROM walk"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        walk = models.Walk(city=row[0], state=row[1], walk_score=row[2],
            transit_score=row[3], bike_score=row[4], population=row[5])
        walk.save()

def import_weather():
    cursor = setup_cursor()
    if cursor is None:
        print('no cursor')
        return
    sql = """SELECT * FROM weather"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        weather = models.Weather(city=row[0], state=row[1], avg_temp_jan=row[2],
            avg_temp_april=row[3], avg_temp_july=row[4], avg_temp_oct=row[5],
            avg_annual_precip_in=row[6],avg_annual_precip_in_days=row[7], 
            avg_annual_precip_snowfall=row[8])
        weather.save()

def import_rent():
    cursor = setup_cursor()
    if cursor is None:
        print('no cursor')
        return
    sql = """SELECT * FROM rent"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        rent = models.Weather(city=row[0], state=row[1], BED_1_MED_PRICE=row[2], 
                    BED_2_MED_PRICE=row[3]) 
        rent.save()

# import_walk()
import_weather()

