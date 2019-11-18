def test(*args):
    print(type(args))
    for i in args:
        print(i)

def test2(**kwargs):
    for i in kwargs:
        print(kwargs[i])


def test3(ad,soyad,*args):
    print(ad)
    print(soyad)
    print(len(args))

def test4(ad,soyad,**kwargs):
    print(ad)
    print(soyad)
    print(type(kwargs))

#test("asd",123,"d",50)

#test2(ad="veysel",yas=30,maas=100)

#test3("veysel","gunduzalp",1,2,3,"a","b")

test4("ali","demir",a=1,uyelik_tarihi="2019.01.01",is_active=True)

dic = {"ad":"veysel","soyad":"gunduzalp"}
tup = (1,3,4)