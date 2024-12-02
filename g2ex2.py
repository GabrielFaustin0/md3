def maiores_3(n1,n2,n3):
    if n1 > 0 and n2 >0 and n3 > 0 :
        if n1 > n2 :
            maior=n1
            if maior>3:
                return maior
            return n3
        else:
            maior=n2
            if maior>n3:
                return maior
            return n3
    elif n1 < 0 and n2 < 0 and n3 < 0 :
        if n1 < n2 :
            maior=n1
            if maior<3:
                return maior
            return n3
        else:
            maior=n2
            if maior<n3:
                return maior
            return n3
    else:
        return None