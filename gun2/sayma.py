sesli_harfler = "aeiıoöüu"

def sesli_harfmi(harf):
    return harf in sesli_harfler

def yazi_al():
    return input("yazi giriniz: ")

def sesli_harf_say(yazi):
    sesli_harf_sayisi = 0
    for harf in yazi:
        if sesli_harfmi(harf):
            sesli_harf_sayisi += 1

    return sesli_harf_sayisi

def ekrana_yaz(yazi,sesi_harf_sayisi):
    print(yazi+" cumlesinde/kelimesinde "+str(sesi_harf_sayisi) + " adet sesli harf bulunmaktadir.")

yazi = yazi_al()
sayi = sesli_harf_say(yazi)
ekrana_yaz(yazi,sayi)




