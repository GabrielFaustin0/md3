def palindromo(palavra):
    inv=""
    palavra=palavra.lower()
    for i in range(len(palavra)-1,-1,-1 ):
        inv=inv+palavra[i]
    if palavra == inv:
        return True
    return False
from termcolor import colored
if palindromo("Açla"):
    print("é")
else:
    print(colored("não","red"))