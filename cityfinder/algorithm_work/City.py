# CityFinder
# A class for cities
# 2-28-2016

import numpy as np

class City(self):

	def __init__(self, name):
		self.name = name
		self.rank = None
		self.score = None
		self.all_scores = np.empty((1,2))
		self.weight = None

	def calculate_score(self):
		'''
		Calculate overall score from individual criteria.
		'''


	def __str__(self):
		print(self.name, ': ', self.rank)

	def __repr__(self):
		str(self)