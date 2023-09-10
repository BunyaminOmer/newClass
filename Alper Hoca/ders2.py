# PYTHON NESNEL TABANLI PROGRAMLAMA - 2 - Class Variables, Sınıf Değişkenleri
#### Python Version: 3.7.4 / VS Code

class Personel:
   
   personel_sayisi = 0
   zam_orani = 1.05

   def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()             # başta böyle değil en altta verceğim ilk halini  
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com" # isime verilecek bilgiyi buraya verdik ve lower metodu ile küçülttük
        
        Personel.personel_sayisi += 1


   def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

   def zam_uygula(self, maas):
      self.maas = int(self.maas * Personel.zam_orani or  self.zam_orani)

per_1 = Personel("John", "Smith", 30000)
per_2 = Personel("Mary", "Smith", 35000)

from pprint import pprint

pprint(per_1.__dict__)
per_1.zam_orani = 1.1
print("__________Manupuleden Sonra:____________")
pprint(per_1.__dict__)

print(Personel.zam_orani) # 1.05
print(per_1.zam_orani)    # 1.1
print(per_2.zam_orani)    # 1.05