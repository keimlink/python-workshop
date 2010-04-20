"""Common functions
"""
from d_tuples import paul, paul2

print __doc__
print 'Hamburg' in paul # True
print 'Leipzig' not in paul # True
print '-' * 40
print paul == paul2 # True
print paul is paul2 # False
print id(paul)
print id(paul2)
paul3 = paul
print paul3 == paul # True
print paul3 is paul # True
print '-' * 40
print paul[1] # 'Hamburg'
print paul[1][3:] # 'burg'
print paul[1][3:5] # 'bu'
print paul[1][3:5] * 3 # 'bububu'
print len(paul) # 3
print len(paul[1]) # 7
print '-' * 40
integers = range(0,3)
print 'integers', integers
a, b, c = integers
print 'a', a # 0
print 'b', b # 1
print 'c', c # 2
print integers[0] is a # True
print id(integers[0])
print id(a)
a, b = integers # Will raise a ValueError
