class Calisan():
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def avans_hesapla(self):
        return self.maas * 30/100
