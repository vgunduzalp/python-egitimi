from Calisan import  Calisan
from Sirket import  Sirket

class Mudur(Sirket):

    def ise_alim(self,kisi):
        self.calisanlar.append(kisi)
        print("işe alım yapıldı, şirketti çalışan sayısı = ",len(self.calisanlar))

    def kasaya_para_ekle(self,miktar):
        self.kasadaki_para += miktar
        print("kasaya {0}TL para aktarildi, kasa durum={1}".format(miktar,self.kasadaki_para))

    def avans_ver(self,ad):


        #calisan = [item for item in self.calisanlar if item.get('ad')==ad]

        calisan = ""
        for i in self.calisanlar:
            if i.ad == ad:
                calisan = i
                break

        kasakipara = self.kasadaki_para
        max_avans = calisan.avans_hesapla()

        if kasakipara < max_avans:
            print("kasa da para yok avans vermezsiniz")
        else:
            print("{0} {1} calişanına {2}TL avans verilmiştir".format(calisan.ad,calisan.soyad,max_avans))


    def para_cek(self,miktar):
        self.kasadaki_para -= miktar
        print("kasadan {0}TL para çekildi, kasa durum={1}".format(miktar, self.kasadaki_para))
