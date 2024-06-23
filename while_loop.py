# WHİLE LOOPS

# 1'den 100'e kadar olan sayıları ekrana yazdırma
x = 0
while x < 100:
    print(x)
    x += 1
print("bitti...") # Döngü sonlandığında ekrana mesaj yazdırma



# Değer aralığı arasındaki çift sayıları ekrana yazdırma
x = 0
while x < 100:
    if x % 2 == 0:
        print(x)
    x += 1
print("finish") # Döngü bittiğinde ekrana mesaj yazdırma



# Değer aralığındaki tek ve çift sayılar
while x <= 100:
    if x % 2 == 1:
        print(f"Sayı tek: {x}")
    else:
        print(f"Sayı çift: {x}")
    x += 1



# Boş bir string değişken tanımlama
name = ""
while not name.strip(): # Kullanıcı boş giriş yaparsa tekrar isim isteme
    name = input("İsminizi giriniz: ")
print(f"Merhaba, {name}") # İsim girildiğinde selamlama yapma




#  ********************  Örnekler:   *********************

sayilar = [1,3,5,7,9,12,19,21]

# 1 - Sayılar listesini while döngüsü kullanarak ekrana yazdırma
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1


# --------------------------------------------------------

# 2 - Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırma
baslangic = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz: "))
i = baslangic
while i <= bitis:
    i += 1
    if i % 2 == 1:
        print(i)


# --------------------------------------------------------

# 3 - 1 ile 100 arasındaki sayıları azalan şekilde ekrana yazma
i = 100
while i > 0:
    print(i)
    i -= 1


# --------------------------------------------------------

# 4 - Kullanıcıdan alınan 5 sayıyı küçükten büyüğe sıralı olarak ekrana yazdırma
numbers = [] # Boş liste tanımlama
i = 0
while i < 5:
    sayi = int(input("Sayı: "))
    numbers.append(sayi) # Aldığımız sayıyı listeye ekleme
    i += 1
numbers.sort() # Sayıları sıralama

print(numbers)


# --------------------------------------------------------

# 5 - Kullanıcıdan alınan sınırsız ürün bilgisini ürünler listesi içerisinde saklayıp ekrana yazdırma
"""
    ürün adetini kullanıcıya sorun
    dictionary listesi yapısı(name, price) şeklinde olsun
    ürün ekleme işlemi bittiğinde ürünleri while ile
"""
urunler = []
adet = int(input("Kaç adet ürün eklemek istersiniz?: "))
i = 0
while i < adet:
    name = input("Ürün ismi: ")
    price = int(input("Ürün fiyat bilgisi: "))
    urunler.append({"name": name, "price": price}) # Ürün bilgisini sözlük olarak listeye ekleme
    i += 1
for urun in urunler:
    print(f"Ürün adı: {urun["name"]}, ürün fiyatı: {["price"]}") # Ürünleri ekrana yazdırma


# --------------------------------------------------------

# 'ABE' stringinin her bir harfini ekrana yazdırma
name = 'ABE'
for letter in name:
    print(letter)

# 'tolga' stringinde 'g' harfine gelince döngüyü durdurma
name2 = 'tolga'
for i in name2:
    if i == 'g':
        break  # g harfi bulunduğunda döngüyü durdurma
    print(i)

# 'exit' kelimesi girilene kadar kullanıcıdan isim isteme
name = ""
while name != "exit":
    name = input("İsminizi girin.\nÇıkmak için 'exit' yazın.")
    print("Merhaba, ", name)

# 'continue' kullanımı örneği
x = 0
while x < 5:
    x += 1
    if x == 2:
        continue  # x 2 olduğunda döngüyü atlayıp devam etme
    print(x)


# 1-100 arasındaki çift sayıların toplamı
x = 0
toplam = 0
while x <= 100:
    x += 1
    if x % 2 == 1:
        continue  # Tek sayıları atlayıp devam etme
    toplam += x
print(toplam)



