from Calisan import  Calisan
from Sirket import  Sirket
from Mudur import Mudur


c1 = Calisan("ali","demir",100)
c2 = Calisan("mehmet","ak",200)
c3 = Calisan("veysel","gunduzalp",300)

m1 = Mudur()

m1.kasaya_para_ekle(100)
m1.kasaya_para_ekle(200)
m1.kasaya_para_ekle(200)
m1.para_cek(480)

m1.ise_alim(c1)
m1.ise_alim(c2)
m1.ise_alim(c3)


m1.avans_ver("ali")
