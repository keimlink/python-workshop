"""Sets and frozensets
"""
print __doc__
# set
word = set('Anna')
print word
print word.difference('Lena')
print word.union('Lena')
frozen = set(['frost', 'winter'])
print frozen
frozen.add('winter') # Ignored
frozen.add('snow')
print frozen
print '-' * 40
# frozenset
frozen = frozenset(frozen)
print frozen
frozen.add('ice') # Raises an AttributeError
