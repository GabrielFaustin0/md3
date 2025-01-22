def FiZZBuZZ(upTO):
    for i in range(1,upTO+1):
        if i % 3==0 and i %5==0:
            print("FiZZBuZZ",end=" ")
        elif i%3==0:
            print("FiZZ",end=" ")
        elif i%5==0:
            print("BuZZ",end=" ")
        else:
            print(i,end=" ")
upTO=int(input(""))
FiZZBuZZ(upTO)