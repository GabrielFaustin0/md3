def tabuada(x):
    for i in range(1,11):
        r=(x*i)
        print(f"{i}x{x}={r}")
x=int(input("digite um numero"))
def main():
    tabuada(x)
if __name__=="__main__":
    main()