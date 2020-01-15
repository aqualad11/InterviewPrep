'''
A set object is an unordered collection of distinct hashable objects. 
Common uses include membership testing, removing duplicates from a sequence, 
and computing mathematical operations such as intersection, union, difference,
and symmetric difference
'''
a = set([1,2,546,74567,'hello', 986])
b = set([1,2,4,34,123,212,1424,234])

# union(ie. in a or b)
print('union')
print(a.union(b))
uni = a | b
print(str(uni))

# intersection(ie. both in a and b)
print('intersection')
print(a.intersection(b))
inter = a & b
print(str(inter))

# difference(ie. in a but not b)
print('difference')
print(a.difference(b))
diff = a - b
print(str(diff))

# symmetric difference(ie. in a or b, but not a and b)
print('symmetric difference')
print(a.symmetric_difference(b))
sym = a ^ b
print(str(sym))


# Set Mutators

# update. update the set by adding elements from iterable/another set
temp = a
temp.update(b)
# or
temp |= b

# intersection update. Update the set by keeping only the elements found in it and an iterable/another set.
temp = a
temp.intersection_update(b)
# or
temp &= b

# difference update. Update the set by removing elements found in an iterable/another set.
temp = a
temp.difference_update(b)
# or
temp -= b

# symmetric difference update. Update the set by only keeping the elements found in either set, but not in both.
temp = a
temp.symmetric_difference_update(b)
# or 
temp ^= b

