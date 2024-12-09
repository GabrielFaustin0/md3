for i in range(10):
    print(i)
    i=0
def funçaoA():
    x=0
    while x<10:
        x=x+1
        return x
"""
print (funçaoA())
print (funçaoA())
print (funçaoA())
print (funçaoA())
"""
def funcab():
    x=0
    while x<10:
        x=x+1
        yield x
for i in funcab():
    print(i)
