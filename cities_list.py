import json, configs, random

global result
with open('cities.json', 'r', encoding='utf-8') as f:
    file_content = json.load(f)['city']

old_cities = []


def generate_new_city(new_city):
    city_name=str(new_city[-1]).upper()
    if city_name in ['Ь', 'Ъ', 'Ы']:
        city_name = str(new_city[-2]).upper()
    for city in file_content:
        if city_name == (city['name'][0]) and city['city_id'] not in old_cities:
            city_data = [city['name'], city['city_id']]
            old_cities.append(str(city['city_id']))
            print(city['name'] + "! Тебе на " + str(city['name'][-1]).upper())
            return city_data
    print("Кажется, ты выиграл... Поздравляю!")


def check_city(new_city,old_city):
    for city in file_content:
        if new_city == (city['name']) and str(city['city_id']) not in old_cities:
            old_cities.append(str(city['city_id']))
            if str(new_city[-1]).upper() in ['Ь', 'Ъ', 'Ы']:
                print("Принято, мне на " + str(new_city[-2]).upper() + "! Хм, дай подумать...")
            else:
                print("Принято, мне на " + str(new_city[-1]).upper() + "! Хм, дай подумать...")
            return True
    print("Неа, не обманывай, такого города нет или он уже был! Тебе всё также на " + str(old_city[0][-1]).upper())


def generate_rnd_city():
    rnd_id = random.randint(6, 30000)
    for city in file_content:
        if str(rnd_id) == city['city_id']:
            start_city = [city['name'], city['city_id']]
            old_cities.append(city['city_id'])
            return start_city
        else:
            rnd_id = random.randint(6, 30000)


gorod = generate_rnd_city()
while gorod is None:
    gorod = generate_rnd_city()

if str(gorod[0][-1]).upper() in ['Ь', 'Ъ', 'Ы']:
    (gorod[0][-1])=str(gorod[0][-2]).upper()
print("Начнём! Мой город = " + gorod[0] + "\nТебе на " + str(gorod[0][-1]).upper())
new_city=''
while new_city != 'СТОП':
    new_city = input('Введи город:\n')
    if len(new_city) <=2:
        continue
    if new_city == "СТОП":
        if len(old_cities) > 3:
            print("Фух, ну и поиграли! Было весело) Всего городов в нашей партии: " +
                  str(len(old_cities)))
            break
        else:
            print("Можем сыграть еще! Пиши /cities и погнали :)")
            break
    # new_city=new_city[0].upper()
    if new_city[0] != str(gorod[0][-1]).upper():
        print("Ты афигел? Тебе вообще-то на " + str(gorod[0][-1]).upper())
    elif check_city(new_city,gorod) is True:
        gorod=generate_new_city(new_city)
        if gorod is None:
            break
    new_city = new_city.upper()
    user_city_fchar = new_city[0]
    user_city_lchar = new_city[-1]
    if user_city_lchar in ['Ь', 'Ъ', 'Ы']:
        user_city_lchar = new_city[-2]

        # user_city = city_search(user_city_lchar)
        # if user_city is not None:
        #     print(user_city)
        #     print(old_cities)
        # else:
        #     print("Город не найден")
