class Calisan():
    calisan_listesi = []

    def ekle(self,adi="",soyadi="",yas=20,maas=6000):
        bigiler = {
            "adi":adi,
            "soyadi":soyadi,
            "yas":yas,
            "maas":maas,
            "memeleket": "ankara"
        }

        self.calisan_listesi.append(bigiler)

    def calisan_bilgilerini_yazdir(self):
        for calisan_dictionary in self.calisan_listesi:
            str_calisan_bilgisi = ""
            """
            str_calisan_bilgisi = "adi={0}, soyadi={1}, yas={2}, maas={3}"\
                .format(calisan_dictionary["adi"],
                        calisan_dictionary["soyadi"],
                        calisan_dictionary["yas"],
                        calisan_dictionary["maas"]
                        )
            """

            for j in calisan_dictionary:
                str_calisan_bilgisi += "{0}={1},".format(j,calisan_dictionary[j])
            print(str_calisan_bilgisi)


c = Calisan()
c.ekle(yas=30,adi="ali",soyadi="demir")
c.ekle(maas=5000,adi="mehmet",soyadi="gundogan")
c.ekle(yas=50)
c.calisan_bilgilerini_yazdir()

