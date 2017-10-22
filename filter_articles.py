#!/usr/local/bin/python3

'''
File desc: Filter unique English articles
'''

import json

c = 0
co = 0
lang = "en"
articles_dict = {}
for i in range(1, 10):
	file = '../IRE_project_snapshot/0' + str(i) + '-05-2017_2'
	print(file)
	with open(file, 'r') as f:
		for line in f:
			l = line.split('\t', 1)
			o = json.loads(l[1])
			try:
				a = o["lang"]
				text = ""
				if a == lang:
					if "title" in o.keys():
						text += o["title"] + " "
					if "desc" in o.keys():
						text += o["desc"]
					articles_dict[l[0]] = text
					co += 1
			except:
				print("null")
				c -= 1

print(len(articles_dict))

with open('en_articles_unique.json', 'w') as w:
	json.dump(articles_dict, w)
	w.write('\n')

print(c)