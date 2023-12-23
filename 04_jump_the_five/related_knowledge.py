# @ 4.1.1 Creating a dictionary
# use dict() function to create am empty dictionary:
answers = dict()

# or use empty curly brackets:
answers = {}
# add key 'name'
answers['name'] = 'Sir Lancelot'
print(answers)

print(type(answers))

answers['quest'] = 'To seek the Holy Grail'
print(answers)

answers['favorite_color'] = 'blue'
print(answers)

# Create a dictionary using dict() function with key-value pairs
answers = dict(name='Sir Lancelot',
               quest='To seek the Holy Grail', favorite_color='blue')

# or use the curlies {}
answers = {'name': 'Sir Lancelot',
           'quest': 'To seek the Holy Grail', 'favorite_color': 'blue'}

# @ 4.1.2 Accessing dictionary values
print(answers['name'])

# answers['age'] # KeyError: 'age'

# use x in y to first see if a key exists:
print('quest' in answers)
print('age' in answers)

# dict.get() method is a safe way to ask for a value:
print(answers.get('quest'))
# When the requested key does not exist in the dict, None is returned:
print(answers.get('age'))
print(type(answers.get('age')))

# There is an optional second argument
# which is the value to return if the key does not exist:
print(answers.get('age', 'NA'))

# @ 4.1.3 Other dictionary methods
print(len(answers))

# keys
print(answers.keys())

# values
print(answers.values())

# get both together:
for key in answers.keys():
    print(key, answers[key])

print(answers.items())

# The preceding for loop could be written using dict.items() method:
for key, value in answers.items():
    print(f'{key:15} {value}')

# help(dict)

# TIP: Each key in the dict is unique.
answers = {}
answers['favorite_color'] = 'blue'
print(answers)

answers['favorite_color'] = 'red'
print(answers)
