# Bu satırda hocanın yazdığı düz hali var çizgiden sonrakiler benim açıklamalarım

# class
class Person:
    # class attributes
    adress = "no information"
    # constructor (yapıcı method)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı.")

        # methods


# object (instances)

p1 = Person(name = "Ali", year = 1990)
p2 = Person(name = "Yağmur", year = 1995)

# updating (sonradan değiştirme(güncelleme))

p1.name = "Ahmet"
p1.adress = "Kocaeli"

# accessing object attributes

print(f"p1 : name : {p1.name} year : {p1.year} adress : {p1.adress}")
print(f"p2 : name : {p2.name} year : {p2.year} adress : {p2.adress}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)

# ---------------------------------------------------------------------------

# Şimdi geldik bana, kodu yazıp açıklama ekleyeceğim...

# class
class Person:   # class açtım
    # class attributes   # sonra açıklama ne olduğunu belirtmek için class attributes yazdım 
    adress = "no information"   # en son init kullanmadan class a bir şey ekledim

    # attributes zaten init kullanmadan bir şey eklemek gibi
    
    # şimdi geçelim yeni açıklamaya

# ----------------------------------------------------------------------------

# constructor (yapıcı method)  # constructor yapıcı method diye açıklama ekledim
                               # e diyeceksin yapıcı method ne __init__ bir yapıcı methottur ve bunun gibi bir sürü vardır en aşağıya yapıcı method örnekleri koyacağım  
    def __init__(self, name, year):  # methoda parametreler ekledim parametre (year, name)  Uyarı init self olmadan olmaz
        # object attributes
        self.name = name   
        self.year = year
        print("init metodu çalıştı.") #defin çalıştığını görmek için bunu yazdım


"""

Yapıcı method örnekleri;

class Örnek():
    def __init__(self):  # Yapıcı methodun başlangıcı
        pass

    def __del__(self):  # Nesne silindiğinde çalışan method
        pass

    def __str__(self):  # Nesne metin olarak temsil edildiğinde dönen değer
        pass

    def __len__(self):  # Len fonksiyonu çağrıldığında dönen değer
        pass

    def __getitem__(self, index):  # İndeksleme işlemi için kullanılan method
        pass

    def __setitem__(self, index, value):  # İndeksleme işlemiyle değer atanması için kullanılan method
        pass

    def __delitem__(self, index):  # İndeksleme işlemiyle eleman silinmesi için kullanılan method
        pass

    def __iter__(self):  # Nesnenin bir yineleyici (iterator) olarak kullanılmasını sağlayan method
        pass

    def __next__(self):  # Yineleyici (iterator) için bir sonraki elemanın döndürüldüğü method
        pass

    def __call__(self, *args, **kwargs):  # Nesne gibi çağrılabilmek için kullanılan method
        pass

    def __eq__(self, other):  # Eşitlik kontrolü için kullanılan method
        pass

    def __lt__(self, other):  # Küçüklük kontrolü için kullanılan method
        pass

    def __gt__(self, other):  # Büyüklük kontrolü için kullanılan method
        pass

    # ... diğer özel methodlar ...

"""

# ----------------------------------------------------------------------------

# object (instances)

p1 = Person(name = "Ali", year = 1990)   # şimdi diyeceksin bune bunlar name için bir isim vermek gerek o yüzden bir değişken atayıp
p2 = Person(name = "Yağmur", year = 1995)# bunun içinde class a eklemen gereken bilgileri ekledim değişken isimleri farklı olursa yeni bir öğrenci eklemiş olursun aynı özellikte

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# updating (sonradan değiştirme(güncelleme))

p1.name = "Ahmet"
p1.adress = "Kocaeli"    # bunda bir şey yok zaten atıyorum isim değiştireceksin eklediğin değişken ismi . sonrada parametre

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# accessing object attributes

print(f"p1 : name : {p1.name} year : {p1.year} adress : {p1.adress}") # burdada yukarıdaki gibi değişken ismi . parametre bunları süslü parantez bitti
print(f"p2 : name : {p2.name} year : {p2.year} adress : {p2.adress}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)  # bunlara eklenecek bir şey yok o yüzden geçiyorum ve bu dosyada burada biter.