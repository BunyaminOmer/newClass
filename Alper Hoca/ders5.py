# PYTHON NESNEL TABANLI PROGRAMLAMA - 5 - ÖZEL METODLAR (SPECİAL METHODS)
# PYTHON VERSİYONU: 3.7.4 / VS Code

class Personel:

   """
      Bu sınıf tutorial kapsamında hazırlandı.
      Bu sınıfı, kullanarak asadsfdksdşlskj
      Bu sınıf içerisindeki tam_isim() ile....
   """

   zam_orani = 1.05

   def __init__(self, isim, soyisim, maas):
      self.isim = isim.title()
      self.soyisim = soyisim.title()
      self.maas = maas
      self.eposta = f"{self.isim.lower()}.{self.soyisim.lower()}@firmam.com"

   def tam_isim(self):
      return f"{self.isim} {self.soyisim}"
   
   def zam_uygula(self):
      self.maas = int(self.maas * self.zam_orani)

   def __repr__(self):
      return f"Personel('{self.isim}', '{self.soyisim}', '{self.maas}')"
   
   def __str__(self):
      return f"{self.tam_isim()} - {self.eposta}"
   
   def __add__(self, mesaj):
      return self.maas + mesaj.maas
   
   def __len__(self):
      return len(self.tam_isim())

per_1 = Personel("Dean", "Winchester", 10000) # Personel("Dean", "Winchester", 10000)
per_2 = Personel("Sam", "Winchester", 15000)  # Personel("Sam", "Winchester", 15000)

# print(len((per_1)))

# print(len("Winchester"))
# print("Winchester".__len__())

# print(per_1 + per_2)
# print(per_1.__add__(per_2))
# print(Personel.__add__(per_1, per_2))

# print(str(per_1))
# print(repr(per_1))

# print(per_1.__str__())
# print(per_1.__repr__())


# print(1 + 2)
# print("a" + "b")