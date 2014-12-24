"""
a=5
b=10-4-1
print (b)
assert a==b

c=5
print (type(c))
d='tekst'
print (type(d))
assert isinstance (c, int)
assert isinstance (d, str)

d='zomaar wat tekst'
try:
    assert isinstance (d, str) #replace with your assert statement
except AssertionError:
    print ('nuts')
else:
    print ('goe bezig')

import re
fObj = re.findall(r'\bd.*?\b', 'a fast and friendly dog')
print(fObj)

sObj = re.search(r'\bd.*?\b', 'a fast and friendly dog')
print(sObj)

mObj = re.match(r'\bd.*?\b', 'a fast and friendly dog')
print(mObj)
"""

def even(getal):
    if getal % 2 == 0:
        return True
    else:
        return False

print ('assert even(4)')
assert even(4)
print ('assert even(7)')
assert even(7) 
