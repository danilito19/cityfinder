

import os
import csv
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "cityfinder.settings"
django.setup()

path = os.path.expanduser('~/Dropbox/city-data/walk-transit-bike-score.csv')


from cityfinderapp.models import City, Walk

with open(path) as f:
	data = csv.reader(f, delimiter=',')
	for line in data:
		city = City.objects.filter(city__iexact=line[0])
		if city:
			print('Found city', city)

		print line
