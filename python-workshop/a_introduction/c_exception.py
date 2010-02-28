# coding: utf-8
u"""Exception handling in python.
„It is Easier to Ask for Forgiveness than Permission.“
"""
def handle_error(msg):
    print 'An error has occurred: %s' % msg

class Spam(object):
    pass


if __name__ == '__main__':
    print __doc__
    spam = Spam()

    if hasattr(spam, 'eggs'):
        ham = spam.eggs
    else:
        handle_error('Asked permission.')

    try:
        ham = spam.eggs
    except AttributeError:
        handle_error('EAFP')
