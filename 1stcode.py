import json

person_dict = {"name": "sohan",
               "languages": ["English", "bd"],
               "married": True,
               "country": "bangladesh",
               "age":13
              }

with open('person.json', 'w') as json_file:
  json.dump(person_dict, json_file)
