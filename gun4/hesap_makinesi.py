def islem_yap(islem_turu):

    def toplam(*args):
        toplam = 0
        for i in args:

            if type(i) is int:
                toplam += i
        return toplam

    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return  carpim

    if islem_turu == "carpma":
        return carpim
    elif islem_turu=="toplama":
        return toplam


sonuc = islem_yap("toplama")(1,2,4)

f = islem_yap("toplama")
sonuc = f(1,"a",2,3,4,5)

print(sonuc)
