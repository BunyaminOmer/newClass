class Personel:

   zam_orani = 1.05

   def __init__(self, isim, soyisim, maas):
      self.isim = isim.title()
      self.soyisim = soyisim.title()
      self.maas = maas

   @property # eğer bunu hangi fonksiyonun üstünü yazarsak sonuna () bunu koyarsak hata verir o yüzden koymayız
   def eposta(self):
      return f"{self.isim.lower()}.{self.soyisim.lower()}@firmam.com"

   @property
   def tam_isim(self):
      return f"{self.isim} {self.soyisim}"
   
   @tam_isim.setter
   def tam_isim(self, ad):
      isim, soyisim = ad.split(" ")
      self.isim = isim
      self.soyisim = soyisim

   @tam_isim.deleter
   def tam_isim(self):
      print("DEĞİŞKENLER SİLİNDİ!!!")
      self.isim = None
      self.soyisim = None

per_1 = Personel("Dean", "Winchester", 10000)

print("____________")
per_1.tam_isim = "Sam"
print(per_1.isim)
print(per_1.eposta)
print(per_1.tam_isim)

del per_1.tam_isim
print(per_1.tam_isim)