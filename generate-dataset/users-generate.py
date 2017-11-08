#!/usr/local/bin/python3

'''
File desc: count number of unique users we have the data for till now
'''

import json
import random

user_articles = {}

for i in range(1, 10):
	file = '../../json_files_english_articles_users/0' + str(i) + '-05-2017_filtered_user_en_articles.json'
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


print(len(user_articles))
c = 0

age_segments = ['12to18', '18to25', '25to35', '35to50', '50to70']
gender = ['Male', 'Female']
cities = ['ahmedabad', 'andhra_pradesh', 'au', 'bangalore', 'bihar', \
		'ca', 'chennai', 'delhi', 'gujarat', 'hyderabad', 'india', \
		'karnataka', 'kerala', 'kolkata', 'madhya_pradesh', 'mumbai', \
		'others', 'us', 'world']
degree_online_engagement = ['highly_active', 'moderately_active', 'less_active', 'highly_inactive']

# age
category_to_age_mapping = {
	'automobiles': age_segments[2],
	'business': age_segments[3],
	'computing': age_segments[1],
	'criminals': age_segments[2],
	'entertainment': age_segments[1],
	'fashion': age_segments[1],
	'foods': age_segments[0],
	'health': age_segments[4],
	'lifestyle': age_segments[2],
	'pbusiness': age_segments[3],
	'pfashion': age_segments[1],
	'phealth': age_segments[2],
	'plifestyle': age_segments[2],
	'politics': age_segments[3],
	'ptechnology': age_segments[1],
	'ptravel': age_segments[2],
	'science': age_segments[0],
	'sports': age_segments[0],
	'technology': age_segments[1],
	'travel': age_segments[1],
	'others': age_segments[2]
}

# gender
# randomly assign

# city
subcategory_to_city_mapping = {
	'ae_all': 'others',
	'ahmedabad_all':'ahmedabad' ,
	'andhra_pradesh_all':'andhra_pradesh' ,
	'ar_all':'others' ,
	'ar_sports':'others' ,
	'au_all':'au' ,
	'au_entertainment':'au' ,
	'au_entertainment_celebs':'au' ,
	'au_entertainment_music':'au' ,
	'au_news':'au' ,
	'au_news_politics':'au' ,
	'au_sports':'au' ,
	'automobiles':'others' ,
	'bangalore_all':'bangalore' ,
	'barcelona_all':'world' ,
	'bd_all':'world' ,
	'bd_sports':'world' ,
	'be_all':'world' ,
	'be_sports':'world' ,
	'bihar_all':'bihar' ,
	'bollywood':'mumbai' ,
	'br_all':'world' ,
	'br_sports':'world' ,
	'ca_all':'ca' ,
	'ca_entertainment':'ca' ,
	'ca_entertainment_celebs':'ca' ,
	'ca_entertainment_music':'ca' ,
	'ca_news':'ca' ,
	'ca_news_politics':'ca' ,
	'ca_sports':'ca' ,
	'california_all':'ca' ,
	'catalonia_all':'world' ,
	'celebrity':'us' ,
	'ch_all':'others' ,
	'ch_sports':'others' ,
	'chennai_all':'chennai' ,
	'chicago_all':'us' ,
	'cn_all':'world' ,
	'cn_entertainment':'world' ,
	'cn_news':'world' ,
	'cn_sports':'world' ,
	'co_all':'us' ,
	'co_news':'us' ,
	'co_sports':'us' ,
	'cricket':'others' ,
	'cz_all':'others' ,
	'dallas_all':'us' ,
	'de_all':'us' ,
	'de_news':'us' ,
	'de_sports':'us' ,
	'delhi_all':'delhi' ,
	'dk_all':'others' ,
	'eg_all':'others' ,
	'eg_news':'others' ,
	'elections':'others' ,
	'es_all':'others' ,
	'es_entertainment':'others' ,
	'es_sports':'others' ,
	'et_all':'others' ,
	'florida_all':'us' ,
	'fr_all':'world',
	'fr_news':'world' ,
	'fr_sports':'world' ,
	'golf':'others' ,
	'gujarat_all':'gujarat' ,
	'hockey':'others' ,
	'hollywood':'us' ,
	'houston_all':'us' ,
	'hyderabad_all':'hyderabad' ,
	'id_all':'world' ,
	'id_news':'world' ,
	'ie_all':'world' ,
	'ie_entertainment':'world' ,
	'ie_news':'world' ,
	'ie_sports':'world' ,
	'il_all':'world' ,
	'il_entertainment':'world' ,
	'il_news':'world' ,
	'illinois_all': 'us',
	'in_all': 'india' ,
	'in_entertainment': 'india',
	'in_entertainment_bollywood': 'india',
	'in_entertainment_celebs':'india' ,
	'in_entertainment_south_cinema':'india' ,
	'in_entertainment_television':'india' ,
	'in_news':'india' ,
	'in_news_politics':'india' ,
	'in_sports':'india' ,
	'ir_all':'india' ,
	'ir_entertainment':'india' ,
	'ir_news':'india' ,
	'it_all':'india' ,
	'it_news':'india' ,
	'it_sports':'india' ,
	'jp_all':'india' ,
	'jp_news':'india' ,
	'jp_sports':'india' ,
	'karnataka_all':'bangalore' ,
	'ke_all':'kerala' ,
	'kerala_all':'kerala' ,
	'kolkata_all':'kolkata' ,
	'kr_all':'bangalore' ,
	'kr_news':'bangalore' ,
	'lk_all': 'world',
	'lk_entertainment':'world' ,
	'lk_news':'world' ,
	'lk_sports':'world' ,
	'los_angeles_all':'us' ,
	'ma_all':'others' ,
	'madhya_pradesh_all':'madhya_pradesh' ,
	'madrid_all':'world' ,
	'maharashtra_all':'mumbai' ,
	'massachusetts_all':'world' ,
	'mlb':'others' ,
	'movie':'others' ,
	'movies':'others' ,
	'mumbai_all':'mumbai' ,
	'music':'others' ,
	'mx_all':'others' ,
	'mx_entertainment':'others' ,
	'mx_sports':'others' ,
	'my_all':'others' ,
	'my_news':'others' ,
	'my_sports':'others' ,
	'nba':'others' ,
	'new_jersey_all':'us' ,
	'new_york_all':'us' ,
	'nfl':'others' ,
	'ng_all':'others' ,
	'ng_entertainment':'others' ,
	'ng_news':'others' ,
	'nhl':'others' ,
	'nl_all':'others' ,
	'nl_news':'others' ,
	'nl_sports':'others' ,
	'nz_all':'others' ,
	'nz_entertainment':'others' ,
	'nz_news':'others' ,
	'nz_sports':'others' ,
	'odisha_all':'odisha' ,
	'ohio_all':'us' ,
	'pbollywood':'others' ,
	'pcelebrity':'others' ,
	'pcricket':'others' ,
	'pelections':'others',
	'pennsylvania_all':'us',
	'pgolf':'others',
	'ph_all':'others' ,
	'ph_entertainment':'others',
	'ph_news':'others',
	'ph_sports': 'others',
	'philadelphia_all':'others',
	'phockey':'others',
	'phollywood':'others' ,
	'pk_all':'world' ,
	'pk_entertainment':'world' ,
	'pk_news':'world'  ,
	'pk_sports': 'world' ,
	'pl_all': 'world' ,
	'pl_sports': 'world' ,
	'plifestyle': 'world' ,
	'pmlb': 'others' ,
	'pmovie':  'others',
	'pmovies':  'others',
	'pmusic':  'others',
	'pnba':  'others',
	'pnfl':  'others',
	'pnhl':  'others',
	'ppolitics':  'others',
	'prugby':  'others',
	'pscience':  'others',
	'pscitech':  'others',
	'psoccer':  'others',
	'psports':  'others',
	'pt_all':  'others',
	'pt_sports':  'others',
	'pune_all': 'india' ,
	'rajasthan_all': 'india' ,
	'ru_all': 'world' ,
	'ru_news': 'world' ,
	'ru_sports': 'world' ,
	'rugby': 'others',
	'sa_all': 'world'  ,
	'sa_news': 'world' ,
	'san_diego_all': 'us' ,
	'san_francisco_all': 'us' ,
	'scitech': 'world' ,
	'se_all': 'world' ,
	'se_news': 'world' ,
	'se_sports': 'world' ,
	'seattle_all': 'us' ,
	'sg_all': 'world' ,
	'sg_news': 'world' ,
	'soccer': 'world' ,
	'tamil_nadu_all': 'chennai' ,
	'telangana_all': 'hyderabad' ,
	'texas_all':'us' ,
	'th_all': 'world' ,
	'th_sports': 'world' ,
	'tr_all': 'world' ,
	'tr_news': 'world' ,
	'ua_all': 'world' ,
	'uk_all': 'world' ,
	'uk_entertainment': 'world' ,
	'uk_entertainment_celebs': 'world' ,
	'uk_entertainment_music': 'world' ,
	'uk_news': 'world' ,
	'uk_news_politics': 'world' ,
	'uk_sports': 'world' ,
	'us_all': 'us' ,
	'us_entertainment': 'us' ,
	'us_entertainment_celebs': 'us',
	'us_entertainment_music': 'us',
	'us_entertainment_television': 'us',
	'us_news': 'us',
	'us_news_elections': 'us',
	'us_news_politics': 'us',
	'us_sports': 'us',
	'uttar_pradesh_all': 'india' ,
	'valencia_all': 'us',
	'vn_all': 'us',
	'washington_all': 'us',
	'west_bengal_all':'india' ,
	'world_all': 'world' ,
	'world_b2b_automobile_manufacturing': 'world',
	'world_b2b_dairy_processing': 'world',
	'world_b2b_digital_broadcasting': 'world',
	'world_b2b_food_processing': 'world',
	'world_b2b_hydrocarbons_and_petrochemicals': 'world',
	'world_b2b_meat_and_poultry_online': 'world',
	'world_b2b_nursing': 'world',
	'world_b2b_oil_and_gas_production': 'world',
	'world_b2b_photonics': 'world',
	'world_b2b_pollution_control_and_equip': 'world',
	'world_b2b_power_generation_and_trans': 'world',
	'world_b2b_pulp_and_paper': 'world',
	'world_b2b_purchasing_and_procurement': 'world',
	'world_b2b_rf_and_microwave': 'world',
	'world_b2b_semiconductor_manufacturing': 'world',
	'world_b2b_solid_waste_treatment': 'world',
	'world_b2b_supermarket_distribution': 'world',
	'world_b2b_supply_chain_markets': 'world',
	'world_b2b_test_and_measurement': 'world',
	'world_b2b_water_and_wastewater_treatment': 'world',
	'world_b2b_wireless_design': 'world',
	'world_b2b_wireless_networking': 'world',
	'world_business': 'world',
	'world_business_advertising': 'world',
	'world_business_airlines': 'world',
	'world_business_banking': 'world',
	'world_business_marketing': 'world',
	'world_business_markets': 'world',
	'world_business_people': 'world',
	'world_business_products': 'world',
	'world_entertainment': 'world',
	'world_entertainment_celebs': 'world',
	'world_entertainment_hollywood': 'world',
	'world_entertainment_music': 'world',
	'world_lifestyle': 'world',
	'world_lifestyle_auto': 'world',
	'world_lifestyle_fashion': 'world',
	'world_lifestyle_foods': 'world',
	'world_lifestyle_health': 'world',
	'world_lifestyle_travel': 'world',
	'world_news': 'world',
	'world_news_politics': 'world',
	'world_sports': 'world',
	'world_sports_american_football': 'world',
	'world_sports_badminton': 'world',
	'world_sports_baseball': 'world',
	'world_sports_basketball': 'world',
	'world_sports_cricket': 'world',
	'world_sports_formula_one': 'world',
	'world_sports_golf': 'world',
	'world_sports_ice_hockey': 'world',
	'world_sports_olympics': 'world',
	'world_sports_rugby': 'world',
	'world_sports_soccer': 'world',
	'world_sports_tennis': 'world',
	'world_technology': 'world',
	'world_technology_digital_marketing': 'world',
	'world_technology_gadgets': 'world',
	'world_technology_gaming': 'world',
	'world_technology_it_companies': 'world',
	'world_technology_social_media': 'world',
	'world_technology_startups': 'world',
	'za_all': 'world',
	'za_entertainment': 'world',
	'za_news': 'world',
	'za_sports': 'world',
	'automobiles': 'others',
	'business': 'world',
	'computing': 'others',
	'criminals': 'world',
	'entertainment': 'others',
	'fashion': 'others',
	'foods': 'world',
	'health': 'world',
	'lifestyle': 'others',
	'pbusiness': 'world',
	'pfashion': 'others',
	'phealth': 'world',
	'plifestyle': 'others' ,
	'politics': 'world' ,
	'ptechnology': 'world' ,
	'ptravel': 'others',
	'science': 'others',
	'sports': 'others',
	'technology': 'world',
	'travel': 'others', 
	'pentertainment' :'others',
	'others': 'others'
}

# degree of engagement

# 'Highly Active' >= 51,
# 11 <= 'Moderately Active' <= 50,
# 3 <= 'Less Active' <= 10,
# 1 <= 'Highly Inactive' <= 2

def no_read_articles_to_degree_online_engagement_mapping(n, number_of_articles=[0, 2, 10, 50]):
    if n < number_of_articles[0]:
        raise ValueError
    for interval, end in enumerate(number_of_articles):
        if n < end:
            return degree_online_engagement[interval - 1]
    else:
        return degree_online_engagement[len(number_of_articles) - 1]

articles_cats = {}
with open('art-cat-subcat', 'r') as f:
	for line in f:
		l = line.split()
		articles_cats[l[0]] = {'category' : l[1], 'subcategory' : l[2]}

def assign_age(a):
	if a[0] not in articles_cats.keys():
		# print(a[0])
		return category_to_age_mapping['others']
	return category_to_age_mapping[articles_cats[a[0]]['category']]

def assign_city(a):
	# print(a)

	# print(articles_cats[a[0]])
	# print(articles_cats[a[0]]['subcategory'])
	try:
		subc = articles_cats[a[0]]['subcategory']
		if subc == 0 or subc == '0':
			return 'others'
		return subcategory_to_city_mapping[articles_cats[a[0]]['subcategory']]
	except:
		return subcategory_to_city_mapping['others']

user_features = {}
c = 0
for user_id, articles in user_articles.items():
	a = list(articles)
	# try:

	v = {
		'gender' : gender[random.randint(0, 1)],
		'age_segment' :  assign_age(a),
		'degree_online_engagement': no_read_articles_to_degree_online_engagement_mapping(len(a)),
		'city': assign_city(a)
	}
	print(v)
	user_features[user_id] = v

with open('user_data.csv', 'w') as w:
	w.write("user_id" + ", " + "age_segment" + ", " + "gender" + ", " + "city" + ", " + "degree_online_engagement" + '\n')
	for u, o in user_features.items():
		w.write(u + ", " + o['age_segment'] + ", " + o['gender'] + ", " + o['city'] + ", " + o['degree_online_engagement'] + '\n')
print(user_features)
print(len(user_features))
print(c)