# This file is to practice and document how collections work

# Counter. Returns a dict where the key is the element in the list and the value is the amount of times it occurs
from collections import Counter

dicto = [6,55,6,4,6,50,4,40,18,60,10,50]

c = Counter(dicto)

print(c)

# defaultdict. Allows you to initialize keys that aren't already in the dictionary
from collections import defaultdict

dd = defaultdict(list)

print(dd['hello']) # prints an empty list


#namedtuple. Are easy to create, lightweight object types for simple tasks
from collections import namedtuple


Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(dot_product)
# 11

#OrderedDict. A dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.
from collections import OrderedDict

ordered_dictionary = OrderedDict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5

print(ordered_dictionary.keys())
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])


# deque. A deque is a double-ended queue. It can be used to add or remove elements from both ends.
from collections import deque

d = deque()
d.append(1)
print(d)
# deque([1])
d.appendleft(2)
print(d)
# deque([2, 1])
d.clear()
print(d)
# deque([])
d.extend('1')
print(d)
# deque(['1'])
d.extendleft('234')
print(d)
# deque(['4', '3', '2', '1'])
d.count('1')



