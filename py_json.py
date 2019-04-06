#JSON is commonly used with data APIS. We can parse JSON into a Python dictionary.

import json

#Sample JSON
userJSON = '{"first_name": "Ivan", "last_name": "Gutierrez", "age": 28}'

#Parse to a dictionary
user = json.loads(userJSON)

print(user)
print(user['last_name'])

car = {'make': 'ford', 'model': 'Mustang', 'Year': 2018}

carJASON = json.dumps(car)
print(carJASON)