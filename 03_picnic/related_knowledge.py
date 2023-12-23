# @ 3.3 Introducing lists

# Create a new, empty list:
items = list()
# or use empty square brackets:
items = []
# Check its type:
print(type(items))
# Get the number of elements in items:
print(len(items))

# @ 3.3.1 Adding one element to a list
# help(list)
print(items)

items.append('sammiches')
print(len(items))

assert len(items) == 1

print(items)

# @ 3.3.2 Adding many elements to a list
# items.append('chips', 'ice cream')
# TypeError: list.append() takes exactly one argument (2 given)
print(items)

# try to give it a list of items to add:
items.append(['chips', 'ice cream'])

# assert len(items) == 3
# Check its length
print(len(items))

# List can hold any type of data, like strings and numbers and even other lists.
print(items)

# reset items:
items = ['sammiches']

# items.extend('chips', 'ice cream')
# TypeError: list.extend() takes exactly one argument (2 given)

items.extend(['chips', 'ice cream'])
assert len(items) == 3

print(items)

items = ['sammiches', 'chips', 'ice cream']
items.insert(0, 'soda')
print(items)

# @ 3.3.3 Indexing lists
print(items[0])
print(items[-1])

# unsafe code:
# print(items[10]) # IndexError: list index out of range

# @ 3.3.4 Slicing lists
print(items[0:2])

# leave out start, it will default to a value of 0:
print(items[:2])
# leave out stop, it will go to the end of the list:
print(items[2:])

# Oddly, it is completely safe for slices to use list indexes that don't exist.
print(items[10:])

# @ 3.3.5 Finding elements in a list
print(items.index('chips'))
# list.index() is unsafe code:
# print(items.index('fog machine')) # ValueError: 'fog machine' is not in list

print('chips' in items)
print('fog machine' in items)

# @ 3.3.6 Removing elements from a list
# list.pop() method will remove and return the element at the index.
# By default it will remove the last item (-1).
print(items.pop())
print(items)

# Use an index to remove an element at a particular location
print(items.pop(0))
print(items)

items.remove('chips')
print(items)

# items.remove('chips') # ValueError: list.remove(x): x not in list

# Remove a given element after verifying:
item = 'chips'
if item in items:
    items.remove(item)

# @ 3.3.7 Sorting and reversing a list
items = ['soda', 'sammiches', 'chips', 'ice cream']

items.sort()
print(items)

items.reverse()
print(items)

items = ['soda', 'sammiches', 'chips', 'ice cream']
# The sorted() function accepts a list as an argument and returns a new list:
print(sorted(items))

# sorted() function does not alter the given list:
print(items)

print(sorted([4, 2, 10, 3, 1]))

# Sorting a list that mixes strings and numbers will cause an exception:
# sorted(1, 'two', 3, 'four') # '<' not supported between instances of 'str' and 'int'

# sort items in reverse:
items.sort(reverse=True)
print(items)

# an example of a lazy function:
print(reversed(items))
print(list(reversed(items)))

# Using list.sort() instead of sorted() function might end up deleting your data:
items = items.sort()
print(type(items))

# @ 3.3.8 Lists are mutable
items = ['soda', 'sammiches', 'chips', 'ice cream']
if 'chips' in items:
    idx = items.index('chips')
    items[idx] = 'apples'

print(items)

assert 'chips' not in items
assert 'apples' in items

# @ 3.3.9 Joining a list
print(', '.join(items))
print(type(', '.join(items)))

# the original list remains unchanged:
print(items)

# @ 3.4 Conditional branching with if/elif/else
age = 15

if age < 0:
    print('You are impossible.')
elif age < 18:
    print('You are a minor.')
else:
    print('You can vote.')
