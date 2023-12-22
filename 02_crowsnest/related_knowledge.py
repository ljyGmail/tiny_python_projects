# @ 2.1.5 Concatenating strings
word = 'narwhal'
print(word)
# print(werd) # name 'werd' is not defined

# The + operator can be used to join strings together
print('Ahoy, Captain, a ' + word + ' off the larboard bow!')

# @ 2.1.6 Variable types
print(type(word))

# word = narwhal # name 'narwhal' is not defined

# @ 2.1.7 Getting just part of a string
word = 'narwhal'
print(word[0])
# Index into a literal string value
print('narwhal'[0])
# the last character
print(word[6])
# use negative index numbers to count backwards
print(word[-1])
# use slice notation [start:stop] to get a range of characters
print(word[:3])
# the default value for stop is the end of the string
print(word[3:])

# @ 2.1.8 Finding help in the REPL
# help(str)

# @ 2.1.9 String methods
print(word.upper())
# parentheses must be included, or the function itself is printed
print(word.upper)
# the method above does not change the value of word:
print(word)
print(word.isupper())
# chain methods together:
print(word.upper().isupper())
print(len('narwhal'))
print(len(word))

# @ 2.1.10 String comparisons
word = 'octopus'
char = word[0]
print(char)
print(type(char))
print(char == 'a')
print(char == 'o')
# compare char to all the vowels:
print(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u')
# What if the word is "Octopus" or "OCTOPUS"?
word = 'OCTOPUS'
char = word[0]
print(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u')

# lowercase word[0]:
word = 'OCTOPUS'
char = word[0].lower()
print(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u')

# x in y construct
print('a' in 'aeiou')
print('b' in 'aeiou')

word = 'OCTOPUS'
print(word[0].lower() in 'aeiou')

# @ 2.1.11 Conditional branching
article = ''
if word[0].lower() in 'aeiou':
    article = 'an'
else:
    article = 'a'

# if expression:
article = 'an' if char in 'aeiou' else 'a'

# This approach is safer because the if expression is required to have the else.
char = 'o'
article = 'an' if char in 'aeiou' else 'a'
print(article)

# @ 2.1.12 String formatting
# The str.format() method is used to expand the values of variables inside strings.
print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))
# f-string
print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
