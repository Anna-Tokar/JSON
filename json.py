import json

str_json = """
{
"response":{
    "count": 5961878,
    "items": [{
        "first_name": "Елизавета",
        "id": 620471795,
        "last_name": "Сопова",
        "can_access_closed": true
    }, {
        "first_name": "Роман",
        "id": 614752515,
        "last_name": "Малышев",
        "can_access_closed": true
}]
}
}"""
print(type(str_json))

# read one string from json-file - loads
data = json.loads(str_json)
print(type(data))
print(data)
print('       ')
print(type(data['response']['items']))

print('\n')
for items in data['response']['items']:
    print(items['first_name'])
print('\n')


# delete one key
for items in data['response']['items']:
    del(items['id'])
    # add new key
    from random import randint
    items['likes'] = randint(100, 200)
    # add key with type none
    items['messange'] = None
    # add key with type datetime -
    from datetime import datetime
    items['time'] = datetime.now().strftime('%d/%m/%y')
print(data['response']['items'])
print('\n')

# create json-file - dump
with open('my.json', 'w') as file:
    json.dump(data, file, indent = 3)
print('\n')

#read json-file - load
with open('my.json', 'r') as file:
    data_info = json.load(file)
print("----data_info:")
print(data_info)
print('\n')

# create json-string - dumps
new_json = json.dumps(data, indent = 2)
print(new_json)
print('\n')

# from json to list
print(json.loads(new_json))

with open('my.json', 'w') as file:
    json.dump(data, file)