#!/usr/local/bin/python3

'''
File desc: Extract category for "lang" articles
'''

import json

lang_dict = {}
en_articles = {}

c = 0
for i in range(1, 10):
	file = '../IRE_project_snapshot/0' + str(i) + '-05-2017_2'
	print(file)
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
				print("null")

for k, v in lang_dict.items():
	print(k, end=" ")
	print(len(v))

categories = []
for k, v in en_articles.items():
	if "category" in v.keys():
		categories.append(v["category"])
		c += 1

categories = [c.lower() for c in categories]

print(sorted(set(categories)))
print(len(set(categories)))
print(c)