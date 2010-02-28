"""Module nature

Demonstrates how to connect objects.
"""
class Animal(object):
    """An animal"""
    def __init__(self, name):
        """Constructor"""
        self.name = name
    
    def __repr__(self):
        """Returns string representation."""
        return 'Animal: %s' % self.name


class Food(object):
    """The Food"""
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name


class Fly(Animal):
    """A fly"""
    pass


class Mouse(Animal):
    """A mouse"""
    def __init__(self):
        """Constructor"""
        self.name = self.__class__.__name__
        self.eaten = {}
    
    def eat(self, food):
        """Eat some food."""
        if food not in self.eaten.keys():
            self.eaten[food] = []
        self.eaten[food].append(food)
    
    def has_eaten(self, food):
        """Which food was eaten?"""
        if food in self.eaten:
            return '%d time(s) %s.' % (len(self.eaten[food]), food)
        return 'No %s.' % food


if __name__ == '__main__':
    print __doc__
    cheese = Food('cheese')
    meat = Food('meat')
    rice = Food('rice')
    fly = Fly('fly')
    mouse = Mouse()
    mouse.eat(cheese)
    mouse.eat(cheese)
    mouse.eat(meat)
    mouse.eat(cheese)
    mouse.eat(fly)
    print '%s has eaten:' % mouse
    print mouse.has_eaten(cheese)
    print mouse.has_eaten(meat)
    print mouse.has_eaten(rice)
    print mouse.has_eaten(fly)
