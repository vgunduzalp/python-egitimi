class Arac():
    modelYili = 2010
    km = 20000

    def arac_ekle(self,model_yili,km):
        self.modelYili = model_yili
        self.km = km

    def arac_bilgisi_yazdir(self):
        print("{0} modelli arac {1} km yol yapmistir".format(self.modelYili,self.km))