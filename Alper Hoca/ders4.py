class Personel:
   
   zam_orani = 1.05

   def __init__(self, isim, soyisim, maas):
      self.isim = isim.title()
      self.soyisim = soyisim.title()
      self.maas = maas
      self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com"

   def tam_isim(self):
      return f"{self.isim} {self.soyisim}"
   
   def zam_uygula(self):
      self.maas = int(self.maas * self.zam_orani)


class Yazilimci(Personel):
   zam_orani = 1.1

   def __init__(self, isim, soyisim, maas, prog_dili):
      super().__init__(isim, soyisim, maas)
      # print(f"Yeni Personel yazılımcı kategorisine taşındı: {self.isim} {self.soyisim}")
      self.prog_dili = prog_dili

class Mudur(Personel):

   def __init__(self, isim, soyisim, maas, personeller = None):
      super().__init__(isim, soyisim, maas)
      if personeller is None:
         self.personeller = []
      else:
         self.personeller = personeller

   def personel_ekle(self, per):
      if per not in self.personeller:
         self.personeller.append(per)

   def personel_cikar(self, per):
      if per in self.personeller:
         self.personeller.remove(per)

   def personelleri_listele(self):
      for e, per in enumerate(self.personeller):
         e += 1
         print(e, per.tam_isim())

yaz_1 = Yazilimci("Dean", "Winchester", 10000, "python")
yaz_2 = Yazilimci("Sam", "Winchester", 15000, "java")

mdr_1 = Mudur("John","Wick",50000, [yaz_1, yaz_2])

print(mdr_1.tam_isim())
print("______________")
mdr_1.personelleri_listele()
print("______________")
mdr_1.personelleri_ekle(yaz_2)
mdr_1.personel_cikar(yaz_1)
mdr_1.personelleri_listele()

# isinstance()
# print(isinstance(yaz_1, Mudur))
# print(isinstance(123, str))

# issubclass()
print(issubclass(Mudur, Yazilimci))