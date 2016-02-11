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
        rent = models.Rent(city=row[0], state=row[1], bed_1_med_price=row[2], 
                    bed_2_med_price=row[3]) 
        rent.save()

def import_crime():
    cursor = setup_cursor()
    if cursor is None:
        print('no cursor')
        return
    sql = """SELECT * FROM crime"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        crime = models.Crime(city=row[0], state=row[1], population=row[2], 
                    violent_crime=row[3], murder=row[4], rape=row[5],
                    robbery=row[6], aggrev_assault=row[7], property_crime=row[8],
                    bulglary=row[9], larceny_theft=row[10], car_theft=row[11],
                    arson=row[12])
        crime.save()

def import_COL():
    cursor = setup_cursor()
    if cursor is None:
        print('no cursor')
        return
    sql = """SELECT * FROM col_index"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        col = models.COL(city=row[0], state=row[1], total_index=row[2], 
                    grocery=row[3], housing=row[4], utilities=row[5],
                    transport=row[6], health=row[7], misc=row[8])
        col.save()

def import_academic():
    cursor = setup_cursor()
    if cursor is None:
        print('no cursor')
        return
    sql = """SELECT * FROM academic"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        ac = models.academic(institution_id=row[0], institution_name=row[1], institution_add=row[2], 
                    institution_city=row[3], institution_state=row[4], institution_zip=row[5],
                    campus_name=row[6], campus_add=row[7], campus_city=row[8],
                    campus_state=row[9], campus_zip=row[10], accreditation=row[11],
                    agency_name=row[12], accreditation_status=row[13], accreditation_date_type=row[14])
        ac.save()

import_crime()
