# coding: utf-8
"""Strings
"""
print __doc__
print 'L' 'o' 's' '!'
print 'Hello', 'world!'
print """This sentence
has multiple
sentences."""
text = "Hello\nworld."
print text
text_raw = r"Hello\nworld."
print text_raw
print '-' * 40
print 'Hi %s' % 'Guido'
print 'Hi %s! My name is %s.' % ('Guido', 'Dennis')
print 'An Unicode character:', unicode(u'\u0153') # will print "œ"
print str(u'\u0153') # Raises an UnicodeEncodeError
