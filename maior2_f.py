def Maiordedois(n1,n2):
    if n1==n2:
        return None
    elif n1>n2:
        return n1
    else:
        return n2
assert Maiordedois(10,5)==10,"não"
assert Maiordedois(10,10)==None, "não iguais"