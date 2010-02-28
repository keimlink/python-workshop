"""Dictionaries
"""
print __doc__
de_en = {'Haus': 'house', 'Tier': 'animal', 'Kind': 'child'}
print de_en
print de_en.keys()
print de_en.values()
print '-' * 40
print de_en['Kind']
print 'Kind' in de_en # True
print de_en.get('Kind', 'not found') # 'child'
print 'child' in de_en.values() # True
print de_en.get('Mutter', 'not found')
print 'Vater' in de_en # False
de_en['Vater'] = 'father'
print de_en.has_key('Vater') # True
print '-' * 40
print zip(de_en.values(), de_en.keys()) # [('animal', 'Tier'), ('father', 'Vater'), ('child', 'Kind'), ('house', 'Haus')]
en_de = dict(zip(de_en.values(), de_en.keys()))
print en_de # {'house': 'Haus', 'father': 'Vater', 'animal': 'Tier', 'child': 'Kind'}
print en_de['child'] # 'Kind'
