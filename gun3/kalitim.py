class Dortgen():
    kisa_kenar=0
    uzun_kenar=0
    dortgen_turu= ""


    def __init__(self,kisa_kenar,uzun_kenar,tur):
        self.kisa_kenar = kisa_kenar
        self.uzun_kenar = uzun_kenar
        self.dortgen_turu = tur

    def alan_hesapla(self):
        alan = self.kisa_kenar * self.uzun_kenar
        print("Dortgenin Alani = ", str(alan))

    def cevre_hesapla(self):
        cevre = (self.kisa_kenar+self.uzun_kenar)*2
        print("Dortgenin Cevresi = ",str(cevre))

    def kenarlari_yaz(self):
        if self.dortgen_turu=="KARE":
            print("Kenar = ", self.kisa_kenar)
        else:
            print("Kisa Kenar = ",str(self.kisa_kenar))
            print("Uzun Kenar = ",str(self.uzun_kenar))

    def tum_bilgileri_yaz(self):
        self.alan_hesapla()
        self.cevre_hesapla()
        self.kenarlari_yaz()


        print("Dörtgen Türü = ",self.dortgen_turu)


class Kare(Dortgen):
    def __init__(self, kenar):
        super().__init__(kenar,kenar,"KARE")
        #self.kisa_kenar = kenar
        #self.uzun_kenar = kenar
        #self.dortgen_turu = "KARE"


class Diktortgen(Dortgen):
    def __init__(self, kisa_kenar, uzun_kenar):
        super().__init__(kisa_kenar,uzun_kenar,"DİKTÖRTGEN")
        #self.kisa_kenar = kisa_kenar
        #self.uzun_kenar = uzun_kenar
        #self.dortgen_turu = "DİKTÖRTGEN"


a = Diktortgen(4,5)
a.tum_bilgileri_yaz()
print("---------------------------------------------")
b = Kare(6)
b.tum_bilgileri_yaz()
