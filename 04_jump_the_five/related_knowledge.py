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

# @ 4.2 Writing jump.py
jumper = {'1': '9',
          '2': '8',
          '3': '7',
          '4': '6',
          '5': '0',
          '6': '4',
          '7': '3',
          '8': '2',
          '9': '1',
          '0': '5'}

assert jumper['1'] == '9'
assert jumper['5'] == '0'

for char in 'ABC123':
    print(char)

# @ 4.4.2 Using a dict for encoding
print(jumper['1'])

print(type('4'))
print(type(4))
print(type(int('4')))

# @ 4.4.2 Various ways to process items in a series
# @@ METHOD 1: USING A FOR LOOP TO PRINT() EACH CHARACTER
text = 'ABC123'
for char in text:
    print(char, char in jumper)

for char in text:
    print(char, jumper[char] if char in jumper else char)

# print(jumper['A']) # KeyError 'A'

print(jumper.get('A'))

for char in text:
    print(char, jumper.get(char))

print(jumper.get('A', 'A'))
print(jumper.get('5', '5'))

for char in text:
    print(jumper.get(char, char))

for char in text:
    print(jumper.get(char, char), end='')
print()

# @@ METHOD 2: USING A FOR LOOP TO BUILD A NEW STRING
new_text = ''

new_text += 'a'
assert new_text == 'a'
new_text += 'b'
assert new_text == 'ab'

new_text = ''
for char in text:
    new_text += jumper.get(char, char)

print(new_text)

# @@ METHOD 3: USING A FOR LOOP TO BUILD A NEW LIST
new_text = []

for char in text:
    new_text.append(jumper.get(char, char))
print(''.join(new_text))

new_text = []
for char in text:
    new_text += jumper.get(char, char)
print(''.join(new_text))

# @@ METHOD 4: USING A FOR LOOP INTO A LIST COMPREHENSION
print(''.join([jumper.get(char, char) for char in text]))

text = '867-5309'
print([jumper.get(char, char) for char in text])
print(''.join([jumper.get(char, char) for char in text]))

# @@ METHOD 5: USING THE STR.TRANSLATE() FUNCTION
text = 'Jenny = 867-5309'
print(text.translate(str.maketrans(jumper)))

# @ 4.4.4 (Not) using str.replace()
text = '1234567890'
text = text.replace('1', '9')
print(text)
text = text.replace('9', '1')
print(text)

text = '1234567890'
for n in jumper.keys():
    text = text.replace(n, jumper[n])

print(text)
