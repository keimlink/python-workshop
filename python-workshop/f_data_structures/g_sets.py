"""Sets and frozensets
"""
print __doc__

# set
wort = set('Anna')
print wort
print wort.difference('Lena')
print wort.union('Lena')
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
