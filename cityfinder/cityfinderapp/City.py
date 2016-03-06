# CityFinder
# A class for cities

import numpy as np
import pandas as pd

class City:

	def __init__(self, city, state, id_, size):
		self.name = city
		self.state = state
		self.city_id = id_
		self.rank = None
		self.score = None
		self.all_scores = None
		self.size = size

	def calculate_score(self, weights, priorities):
		'''
		Calculate overall score from individual criteria.
		'''
		weights_df = pd.DataFrame(weights)
		weights_df.index = priorities
		weights_df = pd.concat([self.all_scores.transpose(), weights_df], axis=1)
		weights_df.columns = [0, 1]
		weights_df['weighted_score'] = weights_df[0] * weights_df[1]
		self.score = float(weights_df.sum(axis = 0)['weighted_score'])

	def __str__(self):
		return ('{} : {}, {:.2f}'.format(self.name, self.rank, self.score))

	def __repr__(self):
		return str(self)