""" 
    Hata ayıklamada breakpoint
"""


class Person:
    # Person sınıfı tanımlanıyor

    def __init__(self, name, age):
        # __init__ metodu, Person nesnesi oluşturulurken çağrılır.
        # name ve age parametreleri alır ve bu değerleri self.name ve self.age olarak saklar.
        self.name = name
        # Burada bir breakpoint koyarak yaşın arttırdığı noktayı inceleyebilirsiniz.
        self.age = age

    def increaseAge(self):
        # increaseAge metodu, kişinin yaşını 1 artırır.
        # Burada bir breakpoint koyarak yaşın azaldığı noktayı inceleyebilirsiniz.

        self.age += 1

    def decreaseAge(self):
        # decreaseAge metodu, kişinin yaşını 1 azaltır, ancak yaş 0'dan küçük olamaz.
        if self.age > 0:
            self.age -= 1

    def __str__(self):
        # __str__ metodu, Person nesnesinin string temsili için kullanılır.
        # Bu metod, "name is age years old!" formatında bir string döner.
        return f"{self.name} is {self.age} years old!"

# Person sınıfından bir aley nesnesi oluşturuluyor.
# Burada bir breakpoint koyarak aley nesnesinin oluşturulduğu ve yaşının 5 olarak ayarlandığı noktayı inceleyebilirsiniz.
aley = Person("aley", 5)

# aley nesnesinin yaşını 6 kez azaltıyoruz.
# Yaş azaltma işlemlerini birer birer test ederken breakpointler koyarak her adımda yaşın nasıl değiştiğini görebilirsiniz.
aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()

# aley nesnesinin string temsili yazdırılıyor, bu durumda "aley is 0 years old!" olarak görünecek. Kodu bir kere daha çağırırsak, değer 0'ın altına düşecektir.
print(aley)

class MyClass:
    # MyClass sınıfı tanımlanıyor

    def __init__(self):
        # __init__ metodu, MyClass nesnesi oluşturulurken çağrılır.
        # Bu metod, "initialized" mesajını yazdırır.
        print("initialized")

    def printSomething(self):
        # printSomething metodu, "python" mesajını yazdırır.
        # Burada bir breakpoint koyarak bu metodun çağrıldığı ve "python" mesajının yazdırıldığı noktayı inceleyebilirsiniz.
        print("python")

# MyClass sınıfından bir myClass nesnesi oluşturuluyor.
# MyClass nesnesini oluştururken ve metodunu çağırırken breakpointler kullanarak her iki adımı da inceleyebilirsiniz.
myClass = MyClass()

# myClass nesnesinin printSomething metodu çağrılıyor.
# Bu metod "python" mesajını yazdırır.
myClass.printSomething()



"""
Breakpoint kullanımı için 'pdb'de kullanılabilir. Örnek:

import pdb

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increaseAge(self):
        pdb.set_trace()  # Burada breakpoint koyarak yaşın arttığı noktayı inceleyebilirsiniz.
        self.age += 1

    def decreaseAge(self):
        if self.age > 0:
            pdb.set_trace()  # Burada breakpoint koyarak yaşın azaldığı noktayı inceleyebilirsiniz.
            self.age -= 1

    def __str__(self):
        return f"{self.name} is {self.age} years old!"

aley = Person("aley", 5)

aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()
aley.decreaseAge()

print(aley)

class MyClass:
    def __init__(self):
        print("initialized")

    def printSomething(self):
        pdb.set_trace()  # Burada breakpoint koyarak bu metodun çağrıldığı ve "python" mesajının yazdırıldığı noktayı inceleyebilirsiniz.
        print("python")

myClass = MyClass()
myClass.printSomething()



"""
