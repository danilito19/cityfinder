from __future__ import unicode_literals

from django.db import models

class Walk(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    walk_score = models.FloatField(max_length=5, blank=True, null=True)
    transit_score = models.FloatField(max_length=5, blank=True, null=True)
    bike_score = models.FloatField(max_length=5)
    population = models.IntegerField(max_length=500)

    def __str__(self):
        return self.city

class Weather(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    avg_temp_jan = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_april = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_july = models.FloatField(max_length=5)
    avg_temp_oct = models.FloatField(max_length=500)
    avg_annual_precip_in = models.FloatField(max_length=500)
    avg_annual_precip_in_days = models.FloatField(max_length=500)
    avg_annual_precip_snowfall = models.FloatField(max_length=500)

class Rent(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    bed_1_med_price = models.FloatField(max_length=500) 
    bed_2_med_price = models.FloatField(max_length=500) 


class Crime(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    population = models.IntegerField(max_length=500)
    violent_crime = models.IntegerField(max_length=500)
    murder = models.IntegerField(max_length=500)
    rape = models.IntegerField(max_length=500)
    robbery = models.IntegerField(max_length=500)
    aggrev_assault = models.IntegerField(max_length=500)
    property_crime = models.IntegerField(max_length=500)
    bulglary = models.IntegerField(max_length=500)
    larceny_theft = models.IntegerField(max_length=500)
    car_theft = models.IntegerField(max_length=500)
    arson = models.IntegerField(max_length=500)

class COL(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    total_index = models.FloatField(max_length=500) 
    grocery = models.FloatField(max_length=500) 
    housing = models.FloatField(max_length=500) 
    utilities = models.FloatField(max_length=500) 
    transport = models.FloatField(max_length=500) 
    health = models.FloatField(max_length=500) 
    misc = models.FloatField(max_length=500) 

class academic(models.Model):
    institution_id = models.IntegerField(max_length=500)
    institution_name = models.CharField(max_length=20, blank=True, null=True)
    institution_add = models.CharField(max_length=20, blank=True, null=True)
    institution_city = models.CharField(max_length=20, blank=True, null=True)
    institution_state = models.IntegerField(max_length=5, blank=True, null=True)
    institution_zip = models.CharField(max_length=7, blank=True, null=True)
    campus_name = models.CharField(max_length=20, blank=True, null=True)
    campus_add = models.CharField(max_length=20, blank=True, null=True)
    campus_city = models.CharField(max_length=20, blank=True, null=True)
    campus_state = models.CharField(max_length=5, blank=True, null=True)
    campus_zip = models.IntegerField(max_length=10, blank=True, null=True)
    accreditation = models.CharField(max_length=20, blank=True, null=True)
    agency_name = models.CharField(max_length=20, blank=True, null=True)
    accreditation_status = models.CharField(max_length=20, blank=True, null=True)
    accreditation_date_type = models.CharField(max_length=20, blank=True, null=True)


