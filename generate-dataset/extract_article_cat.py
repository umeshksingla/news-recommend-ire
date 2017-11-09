#!/usr/local/bin/python3

'''
File desc: Extract all english article's only category and subcatgeory
'''

import json

lang_dict = {}
en_articles = {}

for i in range(1, 10):
	file = '../../IRE_project_snapshot/0' + str(i) + '-05-2017_2'
	with open(file, 'r') as f:
		for line in f:
			l = line.split('\t', 1)
			o = json.loads(l[1])
			try:
				lang = o["lang"]
				if lang not in lang_dict.keys():
					lang_dict[lang] = set()
					lang_dict[lang].add(l[0])
				else:
					lang_dict[lang].add(l[0])
				if lang == "en":
					en_articles[l[0]] = o
			except:
				pass

categories = []
subcategories = []

article_features = {}

def extract_subcategory(c, sc):
	c = c.lower()
	sc = [x.lower() for x in sc]
	#print(sc)
	if len(sc) == 0:
		return 0
	elif len(sc) == 1 and c in sc:
		return 0
	elif len(sc) == 1 and c not in sc:
		return sc[0]
	else:
		if c in sc and c == sc[0]:
			return sc[1]
		else:
			return sc[0]

for article_id, article_obj in en_articles.items():
	if "category" in article_obj.keys():
		category = article_obj["category"].lower()
		subcategory = extract_subcategory(article_obj["category"], article_obj["categories"])
		print(article_id, category, subcategory)
