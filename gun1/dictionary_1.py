veri = {
    "isim":"veysel",
     "soyisim":"gunduzalp",
     4:'test',
     6: 'veysel',
     'ad2':'veysel2'
     }

veri["yeni_eklenen"] = "yenideger" #yeni deger ekleme
veri["isim"] = "v" # var olan degeri degistirme

print(veri["isim"])

for item in veri:
    print(str(item)+'='+veri[item])