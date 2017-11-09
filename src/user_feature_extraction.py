#!/usr/local/bin/python3

'''
File desc: Feature extraction for users, taking following features:

5 age segments
2 gender
19 cities
4 degrees of engagement

'''

from io import StringIO
import json

user_features = {}

# gender
genders = ['Male', 'Female']

# age segment
age_segments = ['12to18', '18to25', '25to35', '35to50', '50to70']

# city
cities = ['ahmedabad', 'andhra_pradesh', 'au', 'bangalore', 'bihar', \
		'ca', 'chennai', 'delhi', 'gujarat', 'hyderabad', 'india', \
		'karnataka', 'kerala', 'kolkata', 'madhya_pradesh', 'mumbai', \
		'others', 'us', 'world']

# degree of engagement
degree_online_engagement = ['highly_active', 'moderately_active', 'less_active', 'highly_inactive']

sample_feature_vec = dict.fromkeys(genders + age_segments + cities + degree_online_engagement, 0)
user_data = '../files/user_data.csv'

with open(user_data, 'r') as f:
	next(f)
	for line in f:
		l = line.split('\n')
		l = l[0].split(',')
		
		user_id = l[0]
		age_segment = l[1]
		gender = l[2]
		city = l[3]
		degree = l[4]

		user_features[user_id] = sample_feature_vec.copy()
		user_features[user_id][age_segment] = 1
		user_features[user_id][gender] = 1
		user_features[user_id][city] = 1
		user_features[user_id][degree] = 1

with open('user_features_engineered.csv', 'w') as w:
	for user_id, features in user_features.items():
		w.write(user_id + ',' + ','.join(str(x) for x in features.values()) + '\n')
