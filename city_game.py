import json, configs, random

global result
with open('cities.json', 'r', encoding='utf-8') as f:
    file_content = json.load(f)['city']

old_cities = []

def generate_rnd_city():
    rnd_id = random.randint(6, 3000)
    for city in file_content:
        if str(rnd_id) == city['city_id']:
            start_city = [city['name'], city['city_id']]
            old_cities.append(city['city_id'])
            return start_city
        else:
            rnd_id = random.randint(6, 3000)
