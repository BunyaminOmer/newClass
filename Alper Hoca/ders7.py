# PYTHON NESNEL TABANLI PROGRAMLAMA - 6 - PROPERTY DECORATORS, GETTERS, SETTERS, DELETERS
# PYTHON VERSİYONU 3.7.4 / Visual Studio Code

class Personel:

   zam_orani = 1.05

   def __init__(self, isim, soyisim, maas):
      self.isim = isim.title()   # GLOBAL
      self.soyisim = soyisim.title()
      self.maas = maas
      self.__zam_orani = 1.05   # PRIVATE

   def getZamOrani(self):
      return self.__zam_orani

   def setZamOrani(self, oran):
      self.__zam_orani = oran

   def zam_uygula(self):
      self.maas = int(self.maas * self.__zam_orani)

per_1 = Personel("Dean", "Winchester", 10000)

print(per_1.isim)
print(per_1.maas)
print(per_1.zam_orani)
per_1.setZamOrani(1.2)
per_1.zam_uygula()
print("Yeni Maaş Miktarı:", per_1.maas)

print(per_1.__dict__)

print(per_1.getZamOrani()) 
print(per_1.setZamOrani(oran=1.2))
