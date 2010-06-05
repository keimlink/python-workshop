"""Lists
"""
print __doc__
colors = ['blue', 'yellow', 'red']
print colors
print colors.count('red') # 1
print colors.index('red') # 2
print colors[2] # 'red'
colors.extend(['purple', 'orange'])
print colors # ['blue', 'yellow', 'red', 'purple', 'orange']
colors.sort()
print colors # ['blue', 'orange', 'purple', 'red', 'yellow']
print ', '.join(colors) # blue, orange, purple, red, yellow
print '-' * 40
print colors[1] # orange
print colors[:4] # ['blue', 'orange', 'purple', 'red']
print colors[2:4] # ['purple', 'red']
print colors[:-3] # ['blue', 'orange']
