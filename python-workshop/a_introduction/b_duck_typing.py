# coding: utf-8
u"""Python uses duck typing.
„If it looks like a duck and quacks like a duck, it must be a duck.“
"""
class Bird(object):
    pass

class Duck(Bird):
    def quak(self):
        return 'Quak'

class Frog(object):
    def quak(self):
        return 'Quak'


if __name__ == '__main__':
    print __doc__
    animals = [Bird(), Duck(), Frog()]

    for animal in animals:
        try:
            print animal.quak(), animal
        except AttributeError:
            print 'No duck', animal
