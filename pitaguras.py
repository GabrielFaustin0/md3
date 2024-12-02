import math
def pitaguras(c1,c2):
    x=c1**2+c2**2
    x=math.sqrt(x)
    x=round(x,3)
    return x
print(pitaguras(4,3))