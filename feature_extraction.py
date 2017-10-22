#!/usr/local/bin/python3

'''
File desc: Feature extraction for articles, taking 1+20+293 features
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

categories = []
subcategories = []

article_features = {}

sample_feature_vec = {'rating': 10, 'ae_all': 0, 'ahmedabad_all': 0, 'andhra_pradesh_all': 0, 'ar_all': 0, 'ar_sports': 0, 'au_all': 0, 'au_entertainment': 0, 'au_entertainment_celebs': 0, 'au_entertainment_music': 0, 'au_news': 0, 'au_news_politics': 0, 'au_sports': 0, 'automobiles': 0, 'bangalore_all': 0, 'barcelona_all': 0, 'bd_all': 0, 'bd_sports': 0, 'be_all': 0, 'be_sports': 0, 'bihar_all': 0, 'bollywood': 0, 'br_all': 0, 'br_sports': 0, 'business': 0, 'ca_all': 0, 'ca_entertainment': 0, 'ca_entertainment_celebs': 0, 'ca_entertainment_music': 0, 'ca_news': 0, 'ca_news_politics': 0, 'ca_sports': 0, 'california_all': 0, 'catalonia_all': 0, 'celebrity': 0, 'ch_all': 0, 'ch_sports': 0, 'chennai_all': 0, 'chicago_all': 0, 'cn_all': 0, 'cn_entertainment': 0, 'cn_news': 0, 'cn_sports': 0, 'co_all': 0, 'co_news': 0, 'co_sports': 0, 'computing': 0, 'cricket': 0, 'criminals': 0, 'cz_all': 0, 'dallas_all': 0, 'de_all': 0, 'de_news': 0, 'de_sports': 0, 'delhi_all': 0, 'dk_all': 0, 'eg_all': 0, 'eg_news': 0, 'elections': 0, 'entertainment': 0, 'es_all': 0, 'es_entertainment': 0, 'es_sports': 0, 'et_all': 0, 'fashion': 0, 'florida_all': 0, 'foods': 0, 'fr_all': 0, 'fr_news': 0, 'fr_sports': 0, 'golf': 0, 'gujarat_all': 0, 'health': 0, 'hockey': 0, 'hollywood': 0, 'houston_all': 0, 'hyderabad_all': 0, 'id_all': 0, 'id_news': 0, 'ie_all': 0, 'ie_entertainment': 0, 'ie_news': 0, 'ie_sports': 0, 'il_all': 0, 'il_entertainment': 0, 'il_news': 0, 'illinois_all': 0, 'in_all': 0, 'in_entertainment': 0, 'in_entertainment_bollywood': 0, 'in_entertainment_celebs': 0, 'in_entertainment_south_cinema': 0, 'in_entertainment_television': 0, 'in_news': 0, 'in_news_politics': 0, 'in_sports': 0, 'ir_all': 0, 'ir_entertainment': 0, 'ir_news': 0, 'it_all': 0, 'it_news': 0, 'it_sports': 0, 'jp_all': 0, 'jp_news': 0, 'jp_sports': 0, 'karnataka_all': 0, 'ke_all': 0, 'kerala_all': 0, 'kolkata_all': 0, 'kr_all': 0, 'kr_news': 0, 'lifestyle': 0, 'lk_all': 0, 'lk_entertainment': 0, 'lk_news': 0, 'lk_sports': 0, 'los_angeles_all': 0, 'ma_all': 0, 'madhya_pradesh_all': 0, 'madrid_all': 0, 'maharashtra_all': 0, 'massachusetts_all': 0, 'mlb': 0, 'movie': 0, 'movies': 0, 'mumbai_all': 0, 'music': 0, 'mx_all': 0, 'mx_entertainment': 0, 'mx_sports': 0, 'my_all': 0, 'my_news': 0, 'my_sports': 0, 'nba': 0, 'new_jersey_all': 0, 'new_york_all': 0, 'nfl': 0, 'ng_all': 0, 'ng_entertainment': 0, 'ng_news': 0, 'nhl': 0, 'nl_all': 0, 'nl_news': 0, 'nl_sports': 0, 'nz_all': 0, 'nz_entertainment': 0, 'nz_news': 0, 'nz_sports': 0, 'odisha_all': 0, 'ohio_all': 0, 'pautomobiles': 0, 'pbollywood': 0, 'pbusiness': 0, 'pcelebrity': 0, 'pcomputing': 0, 'pcricket': 0, 'pcriminals': 0, 'pelections': 0, 'pennsylvania_all': 0, 'pentertainment': 0, 'pfashion': 0, 'pfoods': 0, 'pgolf': 0, 'ph_all': 0, 'ph_entertainment': 0, 'ph_news': 0, 'ph_sports': 0, 'phealth': 0, 'philadelphia_all': 0, 'phockey': 0, 'phollywood': 0, 'pk_all': 0, 'pk_entertainment': 0, 'pk_news': 0, 'pk_sports': 0, 'pl_all': 0, 'pl_sports': 0, 'plifestyle': 0, 'pmlb': 0, 'pmovie': 0, 'pmovies': 0, 'pmusic': 0, 'pnba': 0, 'pnfl': 0, 'pnhl': 0, 'politics': 0, 'ppolitics': 0, 'prugby': 0, 'pscience': 0, 'pscitech': 0, 'psoccer': 0, 'psports': 0, 'pt_all': 0, 'pt_sports': 0, 'ptechnology': 0, 'ptravel': 0, 'pune_all': 0, 'rajasthan_all': 0, 'ru_all': 0, 'ru_news': 0, 'ru_sports': 0, 'rugby': 0, 'sa_all': 0, 'sa_news': 0, 'san_diego_all': 0, 'san_francisco_all': 0, 'science': 0, 'scitech': 0, 'se_all': 0, 'se_news': 0, 'se_sports': 0, 'seattle_all': 0, 'sg_all': 0, 'sg_news': 0, 'soccer': 0, 'sports': 0, 'tamil_nadu_all': 0, 'technology': 0, 'telangana_all': 0, 'texas_all': 0, 'th_all': 0, 'th_sports': 0, 'tr_all': 0, 'tr_news': 0, 'travel': 0, 'ua_all': 0, 'uk_all': 0, 'uk_entertainment': 0, 'uk_entertainment_celebs': 0, 'uk_entertainment_music': 0, 'uk_news': 0, 'uk_news_politics': 0, 'uk_sports': 0, 'us_all': 0, 'us_entertainment': 0, 'us_entertainment_celebs': 0, 'us_entertainment_music': 0, 'us_entertainment_television': 0, 'us_news': 0, 'us_news_elections': 0, 'us_news_politics': 0, 'us_sports': 0, 'uttar_pradesh_all': 0, 'valencia_all': 0, 'vn_all': 0, 'washington_all': 0, 'west_bengal_all': 0, 'world_all': 0, 'world_b2b_automobile_manufacturing': 0, 'world_b2b_dairy_processing': 0, 'world_b2b_digital_broadcasting': 0, 'world_b2b_food_processing': 0, 'world_b2b_hydrocarbons_and_petrochemicals': 0, 'world_b2b_meat_and_poultry_online': 0, 'world_b2b_nursing': 0, 'world_b2b_oil_and_gas_production': 0, 'world_b2b_photonics': 0, 'world_b2b_pollution_control_and_equip': 0, 'world_b2b_power_generation_and_trans': 0, 'world_b2b_pulp_and_paper': 0, 'world_b2b_purchasing_and_procurement': 0, 'world_b2b_rf_and_microwave': 0, 'world_b2b_semiconductor_manufacturing': 0, 'world_b2b_solid_waste_treatment': 0, 'world_b2b_supermarket_distribution': 0, 'world_b2b_supply_chain_markets': 0, 'world_b2b_test_and_measurement': 0, 'world_b2b_water_and_wastewater_treatment': 0, 'world_b2b_wireless_design': 0, 'world_b2b_wireless_networking': 0, 'world_business': 0, 'world_business_advertising': 0, 'world_business_airlines': 0, 'world_business_banking': 0, 'world_business_marketing': 0, 'world_business_markets': 0, 'world_business_people': 0, 'world_business_products': 0, 'world_entertainment': 0, 'world_entertainment_celebs': 0, 'world_entertainment_hollywood': 0, 'world_entertainment_music': 0, 'world_lifestyle': 0, 'world_lifestyle_auto': 0, 'world_lifestyle_fashion': 0, 'world_lifestyle_foods': 0, 'world_lifestyle_health': 0, 'world_lifestyle_travel': 0, 'world_news': 0, 'world_news_politics': 0, 'world_sports': 0, 'world_sports_american_football': 0, 'world_sports_badminton': 0, 'world_sports_baseball': 0, 'world_sports_basketball': 0, 'world_sports_cricket': 0, 'world_sports_formula_one': 0, 'world_sports_golf': 0, 'world_sports_ice_hockey': 0, 'world_sports_olympics': 0, 'world_sports_rugby': 0, 'world_sports_soccer': 0, 'world_sports_tennis': 0, 'world_technology': 0, 'world_technology_digital_marketing': 0, 'world_technology_gadgets': 0, 'world_technology_gaming': 0, 'world_technology_it_companies': 0, 'world_technology_social_media': 0, 'world_technology_startups': 0, 'za_all': 0, 'za_entertainment': 0, 'za_news': 0, 'za_sports': 0}


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
		print(category, subcategory)
		article_features[article_id] = sample_feature_vec.copy()
		article_features[article_id][category] = 1
		if subcategory != 0:
			article_features[article_id][subcategory] = 1


with open('article_features_engineered.csv', 'w') as w:
	for article_id, features in article_features.items():
		w.write(article_id + ',' + ','.join(str(x) for x in features.values()) + '\n')
