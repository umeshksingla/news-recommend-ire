#!/usr/local/bin/python3

'''
File desc: Count number of unique articles for each language
'''

import json

lang_dict = {}

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
				else:
					lang_dict[lang].add(l[0])
			except:
				print("null")

for k, v in lang_dict.items():
	print(k, end=" ")
	print(len(v))