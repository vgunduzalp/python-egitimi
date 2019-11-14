sayi = 4
ad = "veysel"
try:
    #sayi/0
    int(ad)
except ZeroDivisionError:
    print("sifira bolmeya calistiniz")
except ValueError:
    print("deger hatasi")
except:
    print("hata blogu calisti")
finally:
    print("finally blogu calisti")