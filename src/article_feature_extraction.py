#!/usr/local/bin/python3

'''
File desc: Feature extraction for articles, taking following features:

21 categories
314 subcategories

'''

import json

article_features = {}

# category
categories = ['automobiles', 'business', 'computing', 'criminals', 'entertainment', \
	'fashion', 'foods', 'health', 'lifestyle', 'others', 'pbusiness', 'pfashion', \
	'phealth', 'plifestyle', 'politics', 'ptechnology', 'ptravel', 'science', \
	'sports', 'technology', 'travel']

# subcategory
subcategories = ['ae_all', 'ahmedabad_all', 'andhra_pradesh_all', 'ar_all', \
		'ar_sports', 'au_all', 'au_entertainment', 'au_entertainment_celebs', \
		'au_entertainment_music', 'au_news', 'au_news_politics', 'au_sports', \
		'automobiles', 'bangalore_all', 'barcelona_all', 'bd_all', 'bd_sports', \
		'be_all', 'be_sports', 'bihar_all', 'bollywood', 'br_all', 'br_sports', \
		'business', 'ca_all', 'ca_entertainment', 'ca_entertainment_celebs', \
		'ca_entertainment_music', 'ca_news', 'ca_news_politics', 'ca_sports', \
		'california_all', 'catalonia_all', 'celebrity', 'ch_all', 'ch_sports', \
		'chennai_all', 'chicago_all', 'cn_all', 'cn_entertainment', 'cn_news', \
		'cn_sports', 'co_all', 'co_news', 'co_sports', 'computing', 'cricket', \
		'criminals', 'cz_all', 'dallas_all', 'de_all', 'de_news', 'de_sports', \
		'delhi_all', 'dk_all', 'eg_all', 'eg_news', 'elections', 'entertainment', \
		'es_all', 'es_entertainment', 'es_sports', 'et_all', 'fashion', \
		'florida_all', 'foods', 'fr_all', 'fr_news', 'fr_sports', 'golf', \
		'gujarat_all', 'health', 'hockey', 'hollywood', 'houston_all', \
		'hyderabad_all', 'id_all', 'id_news', 'ie_all', 'ie_entertainment', 'ie_news', \
		'ie_sports', 'il_all', 'il_entertainment', 'il_news', 'illinois_all', 'in_all', \
		'in_entertainment', 'in_entertainment_bollywood', 'in_entertainment_celebs', \
		'in_entertainment_south_cinema', 'in_entertainment_television', 'in_news', \
		'in_news_politics', 'in_sports', 'ir_all', 'ir_entertainment', 'ir_news', 'it_all', \
		'it_news', 'it_sports', 'jp_all', 'jp_news', 'jp_sports', 'karnataka_all', 'ke_all', \
		'kerala_all', 'kolkata_all', 'kr_all', 'kr_news', 'lifestyle', 'lk_all', \
		'lk_entertainment', 'lk_news', 'lk_sports', 'los_angeles_all', 'ma_all', \
		'madhya_pradesh_all', 'madrid_all', 'maharashtra_all', 'massachusetts_all', 'mlb', \
		'movie', 'movies', 'mumbai_all', 'music', 'mx_all', 'mx_entertainment', 'mx_sports', \
		'my_all', 'my_news', 'my_sports', 'nba', 'new_jersey_all', 'new_york_all', 'nfl', 'ng_all', \
		'ng_entertainment', 'ng_news', 'nhl', 'nl_all', 'nl_news', 'nl_sports', 'nz_all', \
		'nz_entertainment', 'nz_news', 'nz_sports', 'odisha_all', 'ohio_all', 'others', \
		'pautomobiles', 'pbollywood', 'pbusiness', 'pcelebrity', 'pcomputing', 'pcricket', \
		'pcriminals', 'pelections', 'pennsylvania_all', 'pentertainment', 'pfashion', 'pfoods', \
		'pgolf', 'ph_all', 'ph_entertainment', 'ph_news', 'ph_sports', 'phealth', \
		'philadelphia_all', 'phockey', 'phollywood', 'pk_all', 'pk_entertainment', 'pk_news', \
		'pk_sports', 'pl_all', 'pl_sports', 'plifestyle', 'pmlb', 'pmovie', 'pmovies', 'pmusic', \
		'pnba', 'pnfl', 'pnhl', 'politics', 'ppolitics', 'prugby', 'pscience', 'pscitech', \
		'psoccer', 'psports', 'pt_all', 'pt_sports', 'ptechnology', 'ptravel', 'pune_all', \
		'rajasthan_all', 'ru_all', 'ru_news', 'ru_sports', 'rugby', 'sa_all', 'sa_news', \
		'san_diego_all', 'san_francisco_all', 'science', 'scitech', 'se_all', 'se_news', \
		'se_sports', 'seattle_all', 'sg_all', 'sg_news', 'soccer', 'sports', 'tamil_nadu_all', \
		'technology', 'telangana_all', 'texas_all', 'th_all', 'th_sports', 'tr_all', 'tr_news', \
		'travel', 'ua_all', 'uk_all', 'uk_entertainment', 'uk_entertainment_celebs', \
		'uk_entertainment_music', 'uk_news', 'uk_news_politics', 'uk_sports', 'us_all', \
		'us_entertainment', 'us_entertainment_celebs', 'us_entertainment_music', \
		'us_entertainment_television', 'us_news', 'us_news_elections', 'us_news_politics', \
		'us_sports', 'uttar_pradesh_all', 'valencia_all', 'vn_all', 'washington_all', \
		'west_bengal_all', 'world_all', 'world_b2b_automobile_manufacturing', \
		'world_b2b_dairy_processing', 'world_b2b_digital_broadcasting', 'world_b2b_food_processing', \
		'world_b2b_hydrocarbons_and_petrochemicals', 'world_b2b_meat_and_poultry_online', \
		'world_b2b_nursing', 'world_b2b_oil_and_gas_production', 'world_b2b_photonics', \
		'world_b2b_pollution_control_and_equip', 'world_b2b_power_generation_and_trans', \
		'world_b2b_pulp_and_paper', 'world_b2b_purchasing_and_procurement', \
		'world_b2b_rf_and_microwave', 'world_b2b_semiconductor_manufacturing', \
		'world_b2b_solid_waste_treatment', 'world_b2b_supermarket_distribution', \
		'world_b2b_supply_chain_markets', 'world_b2b_test_and_measurement', \
		'world_b2b_water_and_wastewater_treatment', 'world_b2b_wireless_design', \
		'world_b2b_wireless_networking', 'world_business', 'world_business_advertising', \
		'world_business_airlines', 'world_business_banking', 'world_business_marketing', \
		'world_business_markets', 'world_business_people', 'world_business_products', \
		'world_entertainment', 'world_entertainment_celebs', 'world_entertainment_hollywood', \
		'world_entertainment_music', 'world_lifestyle', 'world_lifestyle_auto', \
		'world_lifestyle_fashion', 'world_lifestyle_foods', 'world_lifestyle_health', \
		'world_lifestyle_travel', 'world_news', 'world_news_politics', 'world_sports', \
		'world_sports_american_football', 'world_sports_badminton', 'world_sports_baseball', \
		'world_sports_basketball', 'world_sports_cricket', 'world_sports_formula_one', \
		'world_sports_golf', 'world_sports_ice_hockey', 'world_sports_olympics', 'world_sports_rugby', \
		'world_sports_soccer', 'world_sports_tennis', 'world_technology', \
		'world_technology_digital_marketing', 'world_technology_gadgets', 'world_technology_gaming', \
		'world_technology_it_companies', 'world_technology_social_media', 'world_technology_startups', \
		'za_all', 'za_entertainment', 'za_news', 'za_sports']

category_vec = dict.fromkeys(categories, 0)
subcategory_vec = dict.fromkeys(subcategories, 0)

article_data = '../files/article_data.csv'

with open(article_data, 'r') as f:
	next(f)
	for line in f:
		l = line.split('\n')
		l = l[0].split(',')

		article_id = l[0]
		category = l[1]
		subcategory = l[2]

		c_vec = category_vec.copy()
		subc_vec = subcategory_vec.copy()

		c_vec[category] = 1
		subc_vec[subcategory] = 1

		article_features[article_id] = list(c_vec.values()) + list(subc_vec.values())

with open('article_features_engineered.csv', 'w') as w:
	for article_id, features in article_features.items():
		s = str(','.join(str(x) for x in features))
		w.write(article_id + ',' + s + '\n')

