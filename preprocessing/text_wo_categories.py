#!/usr/local/bin/python3

'''
File desc: Get text where category or categories is not given

NOTE: You can change code by removing 'not' if you want the
text where category is given.
'''

import json

lang_dict = {}
en_articles = {}

c = 0
for i in range(1, 10):
	file = '../../IRE_project_snapshot/0' + str(i) + '-05-2017_2'
	#print(file)
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
				#print("null")

o = {}
with open('articles_wo.json', 'w') as w:
	for k, v in en_articles.items():
		if "category" not in v.keys():
			o = {"id": k, "desc": v["desc"]}
			w.write(json.dumps(o) + '\n')