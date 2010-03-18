# coding: utf-8
"""Strings
"""
print __doc__
print 'H' 'e' 'l' 'l' 'o' '!'
print 'Hello', 'world!'
print 'Hello' + ' ' + 'world!'
print """This sentence
has multiple
lines."""
text = "Hello\nworld."
print text
text_raw = r"Hello\nworld."
print text_raw
print '-' * 40
print 'Hi %s!' % 'Guido'
print 'Hi %s! My name is %s.' % ('Guido', 'Dennis')
print 'Hi %(friend)s! My name is %(me)s.' % {'me': 'Brian', 'friend': 'Guido'}
# String formatting with Python 2.6 and 3.0
print 'Hi {0}!'.format('Guido')
print 'Hi {0}! My name is {1}.'.format('Guido', 'Dennis')
print 'Hi {friend}! My name is {me}.'.format(me='Brian', friend='Guido')
print 'This DVD contains {0:.2f} GB of data.'.format(1.7484232)
print '-' * 40
text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print text.count('dolor')
first_sentence = text[:124]
print first_sentence
print first_sentence.title()
print 'istitle:', first_sentence.title().istitle()
print 'isdigit:', first_sentence.isdigit()
print 'isalpha:', first_sentence.isalpha()
print 'startswith:', first_sentence.startswith('Lorem')
print 'endswith:', first_sentence.endswith('.')
print first_sentence.lower()
print 'islower:', first_sentence.lower().islower()
print 'isupper:', first_sentence.isupper()
print first_sentence.replace('ipsum', 'python')
print '-' * 40
print 'An Unicode character:', unicode(u'\u0153') # will print "œ"
print str(u'\u0153') # Raises an UnicodeEncodeError
