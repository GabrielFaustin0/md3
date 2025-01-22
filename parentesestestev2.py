def conta(conta):
    abriu=""
    for i in conta:
        if i =="(" or i =="[":
            abriu=abriu+i
        if i ==")"or i == "]":
            if abriu=="":
                return False
            ultimo=abriu[len(abriu)-1]
            if (ultimo =="(" and i ==")") or (ultimo=="["and i =="]"):
                temp=abriu
                abriu=""
                for i in range(len(temp)-1):
                    abriu=abriu+temp[i]
            else:
                return False
    if abriu=="":
        return True
    return False
contar=input("")
print(conta(contar))