"""Lists
"""
print __doc__
colors = ['blue', 'yellow', 'red']
print colors
print colors.count('red') # 1
print colors.index('red') # 2
print colors[2] # 'red'
colors.extend(['purple', 'orange'])
print colors
colors.sort()
print colors # Now the list is sorted.
print ', '.join(colors)
print '-' * 40
print colors[:4] # ['blue', 'yellow', 'purple', 'orange']
print colors[2:4] # ['purple', 'orange']
print colors[:-3] # ['blue', 'yellow']
