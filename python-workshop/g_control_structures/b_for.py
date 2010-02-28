"""for statement
"""
print __doc__
for i in range(0, 11):
    print i ** 2
print '-' * 40
for i in range(0, 11):
    if i > 6:
        break
    print i ** 2
print '-' * 40
print [a * b for a, b in zip(range(1,6), range(5, 11))] # [5, 12, 21, 32, 45]
