# class
class Person:
    # class attributes
    adress = "no information"

    # constructor (yapıcı method)
    def __init__(self, name, year):
    
        # object attributes
        self.name = name
        self.year = year

    # instance methods
    def intro(self):
        print(f"Hello There. I am {self.name}")

    def calculateAge(self):
        return 2023 - self.year

# object (instances)

p1 = Person(name = "Ali", year = 1990)
p2 = Person(name = "Yağmur", year = 1995)

p1.intro()
p2.intro()

print(f"Adım {p1.name} ve Yaşım {p1.calculateAge()}")
print(f"Adım {p2.name} ve Yaşım {p2.calculateAge()}")

# ----------------------------------------------------------

class Circle:
    # Class Object Attributes
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevreHesapla(self):
        return 2 * self.pi + self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)
    
c1 = Circle()  # yaricap = 1
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla()} çevre : {c1.cevreHesapla()}")
print(f"c2 : alan = {c2.alan_hesapla()} çevre : {c2.cevreHesapla()}")