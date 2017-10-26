#!/usr/local/bin/python3

'''
File desc: <user_id> <article_id> <read/not-read> format from <date>_filtered_user_en_articles.json
'''

import json

user_articles = {}

for i in range(1, 10):
	file = '0' + str(i) + '-05-2017_filtered_user_en_articles.json'
	print(file)
	with open(file, 'r') as f:
		for line in f:
			l = json.loads(line)
			for user_id, articles in l.items():
				if len(articles):
					for a_id in articles:
						if user_id not in user_articles.keys():
							user_articles[user_id] = set()
						user_articles[user_id].add(a_id)

with open('user_article_read.csv', 'w') as w:
	for user_id, articles in user_articles.items():
		for a_id in articles:
			w.write(user_id + ',' + a_id + ',' + '10' + '\n')