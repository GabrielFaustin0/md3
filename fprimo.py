def primo(n)->bool:
    primo=True
    for x in range(2,n):
        if n % x == 0:
            primo = False
            break
        return 
if(primo(5)) ==True:
    print("o numero é primo")
else:
    print(f"não é primo")