"""A singleton class using a decorator and a property.

PEP 318
Decorators for Functions and Methods
http://www.python.org/dev/peps/pep-0318/

Built-in Functions: property
http://docs.python.org/library/functions.html#property
"""

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class Foo(object):
    _bar = None
    
    @property
    def bar(self):
        return self._bar
    
    @bar.setter
    def bar(self, value):
        self._bar = value
    
    @bar.deleter
    def bar(self):
        del self._bar
    #bar = property(get_bar, set_bar, del_bar, "Old style property")
#Foo = singleton(Foo) # Old style decorator


if __name__ == '__main__':
    print __doc__
    f1 = Foo()
    print f1.bar
    f2 = Foo()
    print f2.bar
    f1.bar = 2
    print f1.bar, f2.bar
    del(f2.bar)
    print f1.bar, f2.bar
