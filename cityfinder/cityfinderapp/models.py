from __future__ import unicode_literals
from django.db import models

## ORIGINAL CODE, heavily modified from Django documentation

class City(models.Model):
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=5, blank=True, null=True)
    
    def __str__(self):
        return '%s %s' % (self.city, self.state)

class Walk(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=5, blank=True, null=True)
    walk_score = models.FloatField(max_length=5, blank=True, null=True)
    transit_score = models.FloatField(max_length=5, blank=True, null=True)
    bike_score = models.FloatField(max_length=5, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.city, self.state, self.walk_score)

class Weather(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=5, blank=True, null=True)
    avg_temp_jan = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_april = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_july = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_oct = models.FloatField(max_length=500, blank=True, null=True)
    avg_annual_precip_in = models.FloatField(max_length=500, blank=True, null=True)
    avg_annual_precip_in_days = models.FloatField(max_length=500, blank=True, null=True)
    avg_annual_precip_snowfall = models.FloatField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.city, self.state)

class Rent(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=5, blank=True, null=True)
    bed_1_med_price = models.FloatField(max_length=500, blank=True, null=True) 
    bed_2_med_price = models.FloatField(max_length=500, blank=True, null=True) 

    def __str__(self):
        return '%s %s' % (self.city, self.state)

class Crime(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=5, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    violent_crime = models.IntegerField(blank=True, null=True)
    murder = models.IntegerField(blank=True, null=True)
    rape = models.IntegerField(blank=True, null=True)
    robbery = models.IntegerField(blank=True, null=True)
    aggrev_assault = models.IntegerField(blank=True, null=True)
    property_crime = models.IntegerField(blank=True, null=True)
    bulglary = models.IntegerField(blank=True, null=True)
    larceny_theft = models.IntegerField(blank=True, null=True)
    car_theft = models.IntegerField(blank=True, null=True)
    arson = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.city, self.state)

class COL(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=5, blank=True, null=True)
    total_index = models.FloatField(max_length=500, blank=True, null=True) 
    grocery = models.FloatField(max_length=500, blank=True, null=True) 
    housing = models.FloatField(max_length=500, blank=True, null=True) 
    utilities = models.FloatField(max_length=500, blank=True, null=True) 
    transport = models.FloatField(max_length=500, blank=True, null=True) 
    health = models.FloatField(max_length=500, blank=True, null=True) 
    misc = models.FloatField(max_length=500, blank=True, null=True) 

    def __str__(self):
        return '%s %s' % (self.city, self.state)

''' CURRENTLY DID NOT IMPORT ACADEMIC DATA INTO DB '''
class academic(models.Model):
    institution_id = models.IntegerField(default=None)
    name = models.CharField(max_length=20, blank=True, null=True)
    add = models.CharField(max_length=20, blank=True, null=True)
    city = models.ForeignKey(City)
    state = models.IntegerField( blank=True, null=True)
    zip_code = models.CharField(max_length=7, blank=True, null=True)
    
    def __str__(self):
        return '%s %s' % (self.city, self.state)

class LGBT(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=20, default=None)
    Total_HH = models.IntegerField(blank=True, null=True)
    THH_MOE = models.IntegerField(blank=True, null=True)
    Total_Unmarried = models.IntegerField(blank=True, null=True)
    TU_MOE = models.IntegerField(blank=True, null=True)
    Male_Male_HH = models.IntegerField(blank=True, null=True)
    MMHH_MOE = models.IntegerField(blank=True, null=True)
    Female_Female_HH = models.IntegerField(blank=True, null=True)
    FFHH_MOE = models.IntegerField(blank=True, null=True)
    All_Other_HH = models.IntegerField(blank=True, null=True)
    AOH_MOE = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.city, self.state)

class Hisp(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=20, default=None)
    hisp_count = models.IntegerField(blank=True, null=True)
    hisp_MOE = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.city, self.state)

class Age(models.Model):
    city = models.ForeignKey(City)
    state = models.CharField(max_length=20, default=None)
    population = models.IntegerField(blank=True, null=True)
    median_age = models.FloatField(max_length=500, blank=True, null=True) 
    age_depend_ratio = models.FloatField(max_length=500, blank=True, null=True) 
    old_age_depend_ratio = models.FloatField(max_length=500, blank=True, null=True) 
    child_depend_ratio = models.FloatField(max_length=500, blank=True, null=True) 

    def __str__(self):
        return '%s %s' % (self.city, self.state)

