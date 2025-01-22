def conta(conta):
    p=0
    for i in conta:
        if i == "(":
            p=p+1
        elif i == ")":
            p=p-1

        if p<0:
            return False
    if p==0:
        return True
    return False
contar=input("")
print(conta(contar))