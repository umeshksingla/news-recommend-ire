#!/usr/local/bin/python3

'''
File desc: Remove other language articles from users' given list
'''

import json

lang = "en"
article_ids = []

with open('en_articles_unique_ids.json') as f:
	for line in f:
		en_article_ids = json.loads(line)

for i in range(8, 9):
	user_articles = {}
	n = '0' + str(i) + '-05-2017'
	file = '../IRE_project_snapshot/' + n
	print(file)
	with open(file, 'r') as f:
		for user in f:
			l = user.split('\t')
			user_id = l[1]
			print(user_id)
			article_list = json.loads(l[2])
			new_article_list = []
			for article_id in article_list:
				if article_id in en_article_ids:
					new_article_list.append(article_id)
			user_articles[user_id] = new_article_list

	with open(n + '_filtered_user_en_articles.json', 'w') as w:
		json.dump(user_articles, w)
		w.write('\n')