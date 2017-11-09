#!/usr/local/bin/python3

'''
File desc: Extract all english article's only category and subcatgeory
'''

import json

en_articles = {}
for i in range(1, 10):
	file = '../../IRE_project_snapshot/0' + str(i) + '-05-2017_2'
	print(file)
	with open(file, 'r') as f:
		for line in f:
			l = line.split('\t', 1)
			o = json.loads(l[1])
			try:
				lang = o["lang"]
				if lang == "en":
					en_articles[l[0]] = o
			except:
				print("null")


def extract_subcategory(c, sc):
	c = c.lower()
	sc = [x.lower() for x in sc]
	if len(sc) == 0:
		return 'others'
	elif len(sc) == 1 and c in sc:
		return 'others'
	elif len(sc) == 1 and c not in sc:
		return sc[0]
	else:
		if c in sc and c == sc[0]:
			return sc[1]
		else:
			return sc[0]


with open('article_data.csv', 'w') as w:
	w.write("article_id" + "," + "category" + "," + "subcategory" + '\n')
	for article_id, article_obj in en_articles.items():
		if "category" in article_obj.keys():
			category = article_obj["category"].lower()
			subcategory = extract_subcategory(article_obj["category"], article_obj["categories"])
			w.write(article_id + "," + category + "," + subcategory + '\n')
