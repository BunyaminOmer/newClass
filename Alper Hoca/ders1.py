# PYTHON NESNEL TABANLI PROGRAMLAMA - 1 - Classes and Instances
#### Python Version: 3.7.4 / VS Code

class Personel:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()             # başta böyle değil en altta verceğim ilk halini  
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com" # isime verilecek bilgiyi buraya verdik ve lower metodu ile küçülttük

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
per_1 = Personel(isim = "John", soyisim = "Smith", maas = 30000)
per_2 = Personel("Mary","Smith",35000)

per_1.tam_isim() # dersek hani print yok eklesek
print(Personel.tam_isim(per_1)) # şimdi biz diyelim ki çalışan var müdürler müdür yard ve vb. hep biz çalışan class ını bakmıyacağız ki bide müdürede bakalım müdür yard. o yüzden ilk önce bir class daha kullanacağız mesela bütün isme bakacağız tam_isim diye bir class vardı onu ekleriz parantez içinde kişi seçer çalıştırız

# Personel 1

print(per_1.isim)  # John
print(per_1.soyisim)  # Smith
print(per_1.maas)     # 30000

# Personel 2

print(per_2.isim)
print(per_2.isim)
print(per_2.maas)

print(Personel) # Personel bir class onu söylüyor hatta sonuç vereyim 
print(per_1) # ramdaki adresi yazdırır ve per_2de deram adresi yazar ama farklı adresler yazar. 
print(per_2)

# Bunları yazdırınca

"""

<class '__main__.Personel'>
<__main__.Personel object at 0x00000157B1AF2890>
<__main__.Personel object at 0x00000157B1AF28D0>

"""

# şimdi bir şirketimiz varmış ve şirket çalışanlarının bilgisini girecekmişiz şimdi bununla ilgili bir otomasyon örneği yapalım daha doğrusu konuyu anlatırken örnek yapalım

per_1.isim = "John"
per_1.soyisim = "Smith"
per_1.eposta = "john.smith@firmam.com"

per_2.isim = "Mary"
per_2.soyisim = "Smith"
per_2.eposta = "mary.smith@firmam.com"   # şimdi bunlar karı koca aynı şirkette ve ekrana şöyle yazdırdım

# print(per_1) # tabikide yazmaz çünkü per_1 den ne istediğimizi belirtmedik şöyle düzletirsek

print(per_1.eposta) # ve çıktı ve ikincinin e postaya bakalım
print(per_2.eposta)
"""

self yerine nesne vb. gibi şeyler yazarsak onlarla yapsak öylede olur



def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()             
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com"

Yukarıdakinde self.odeme yapsak çalışır self.ad yazsak çalışır vb.

iki olabilecek farklı bir kullanım yöntemleri var

mesela isim ve soyisim yazdıracaksın iki yöntemde olur

print(f"{} {}".format(per_2.isim, per_2.soyisim))

"""