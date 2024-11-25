def media1():
    x=int(input("digite um numero"))
    y=int(input("digite outro numero"))
    z=int(input("digite outro numero"))
    media=(x+y+z)/3
    print(media)
def media2(x,y,z):
    media=(x+y+z)/3
    print(media)
def media3():
    x=int(input("digite um numero"))
    y=int(input("digite outro numero"))
    z=int(input("digite outro numero"))
    media=(x+y+z)/3
    return media
def media4(x,y,z):
    media=(x+y+z)/3
    return media
media4(5,6,19)
def main():
    media1()
    media2(4,5,2)
    #media3()
    print(media3())
   # media4(5,6,19)
    print(media4(5,6,5))
if __name__=="__main__":
    main()