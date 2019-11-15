def toplama():
    print(1+2)


def ikisayiyi_topla(a,b):
    toplam = a+b
    print(toplam)
    return toplam

#toplama()

sonuc = ikisayiyi_topla(4,5)

print("sonuc:",sonuc)

def kare_al(a,b):
    return a*a,b*b

x,y = kare_al(3,4)

print("x=",x)
print("y=",y)

def kare1(a,b):
    return a*b

kare = lambda a,b:a*b

print(kare(10,4))