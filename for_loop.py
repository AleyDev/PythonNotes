# FOR LOOPS
# Bir dizi (liste, tuple, string vb.) veya yineleyici üzerinde gezinerek her bir öğe için belirli bir kod bloğunu çalıştıran bir döngü yapısıdır.

# Liste tanımlama
numbers = [1, 2, 3, 4, 5]

# print(numbers[0]) : -> 1
# print(numbers[1]) : -> 2
# print(numbers[2]) : -> 3
# print(numbers[3]) : -> 4
# print(numbers[4]) : -> 5



# Liste elemanlarını sırayla ekrana yazdırma(index-index okutarak etrana yazdırıyoruz)
for sayi in numbers:
    print(sayi)



# String listesi tanımlama
names = ['Aleyna', 'Tolga', 'Enes', 'Ali']

# Liste elemanlarını tek tek çekip ekrana yazdırıyoruz. (f-string kullandım)
for name in names:
    print(f"My name is {name}")



# String tanımlama
name = 'Aley'

# Her bir karakteri ayrı ayrı ekrana yazdırma
for n in name:
    print(n)



# Tuple tanımlama
tuple = (1, 2, 3, 4, 5)

# Her bir tuple elemanını ekrana yazdırma
for t in tuple:
    print(t)




# Tuple içindeki her bir tuple'ı ayrı ayrı ekrana yazdırma
tuple = [(1,2), (2,3), (3,5), (3,7)]
for t in tuple:
    print(t)

# Her bir tuple içindeki elemanları ayrı ayrı ekrana yazdırma
for a,b in tuple:
    print(a,b)



# Sözlük tanımlama
dict = {'k1': 1, 'k2': 2, 'k3': 3}

# Sözlükteki her bir anahtar-değer çiftini ayrı ayrı ekrana yazdırma
for key, value in dict.items():
    print(key, value)

# Sözlükteki her bir anahtarı ayrı ayrı ekrana yazdırma
for key,value in dict.items():
    print(key)

# Sözlükteki her bir değeri ayrı ayrı ekrana yazdırma
for key,value in dict.items():
    print(value)



# 'tolga' stringinde 'g' harfine gelince döngüyü durdurma
name2 = 'tolga'
for i in name2:
    if i == 'g':
        break  # g harfi bulunduğunda döngüyü durdurma
    print(i)



# range fonksiyonu kullanımı
for item in range(10):  # 0'dan 10'a kadar olan sayıları ekrana yazdırma
    print(item)
# bu işlemin tek satırda kısa yolu:
# print(list(range(5,10,2))) 'dir.

# range fonksiyonunun kullanımı
for item in range(1, 50, 2):  # 1'den 50'ye kadar olan sayıları 2'şer 2'şer ekrana yazdırma
    print(item)



# enumerate fonksiyonu kullanımı
index = 0
greeting ='Hello There'

for letter in greeting:
    # print(letter) #kelime içindeki her harfi tek tek ekrana yazdırır
    print(f'index: {index} letter: {greeting[index]}') # her bir harfi index numaraları ile ekrana yazdırma işlemi
    # print(f'index: {index} letter: {letter}') 
    index += 1 #indexleri gezebilmesi için

#yukarıdaki işlemin kısa yolu: enumerate ile****
greeting = 'Hello'

for index,letter in enumerate(greeting):
    print(f'index: {index} letter: {letter}')

for item in enumerate(greeting): # alır her bir elemanı alır
    print(item) 



# Zip fonksiyonu kullanımı
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]
print(list(zip(list1, list2, list3)))  # Üç listeyi zip ile eşleştirip birleştirme



# --------------------------------------------------------

# List comprehension kullanımı
# 1: 0'dan 9'a kadar olan sayıları liste olarak alma
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)
# Kısa hali
numbers = [x for x in range(10)]
print(numbers)


# 2: 0'dan 9'a kadar olan sayıların karesini alma
for x in range(10):
    print(x**2)
# Kısa hali
numbers = [x**2 for x in range(10)]
print(numbers)


# 3: 0'dan 9'a kadar olan sayıların karesini, sadece 3'e bölünebilenlerin listesi
numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers)


# 4: 'Hello' kelimesinin her bir harfini listeye alma
myString = 'Hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)
# Kısa hali
myList = [letter for letter in myString]
print(myList)


# 5: Yılları yaşa dönüştürme
years = [1983, 1999, 2008, 1956, 1986]
ages = [2024 - year for year in years] # Yaş hesabı
print(ages)


# --------------------------------------------------------

# Ternary operatörü kullanımı
results = [x if x % 2 == 0 else 'tek' for x in range(1, 10)]
print(results)

# 1: 0-2 arası x ve y değerlerini tuple olarak ekleme
result = []
for x in range(3): 
    for y in range(3):
        result.append((x,y))
print(result)
# Kısa hali
result = [(x, y) for x in range(3) for y in range(3)]
print(result)

# 2: 0-2 arası x ve y değerlerini tuple olarak ekleme (alternatif yöntem)
numbers = [(x, y) for x in range(3) for y in range(3)]
print(numbers)




#  ********************  Örnekler:   *********************

sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1 - Sayılar listesindeki hangi sayılar 3'ün katıdır?
for i in sayilar:
    if i % 3 == 0:
        print(i)

# 2 - Sayılar listesindeki sayıların toplamı kaçtır?
toplam = 0
for i in sayilar:
    toplam += i
print("Toplam: ", toplam)

# 3 - Sayılar listesindeki tek sayıların karesini alınız.
for i in sayilar:
    if i % 2 == 1:
        print(i**2)


# --------------------------------------------------------

sehirler = [ 'Tekirdağ', 'İstanbul', 'İzmir', 'Rize']

# 4 - Şehirlerden hangileri en fazla 5 karakterlidir?
for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)


# --------------------------------------------------------

urunler = [
    {'name': 'Iphone S6', 'price': '3000'},
    {'name': 'Iphone 8', 'price': '4000'},
    {'name': 'Iphone X', 'price': '5000'},
    {'name': 'Iphone 12', 'price': '6000'},
    {'name': 'Iphone 13', 'price': '7000'},
]

# 5 - Ürünlerin fiyatları toplamı nedir?
toplam = 0
for urun in urunler:
    price = int(urun["price"])
    toplam += price
print("Toplam: ", toplam)

# 6 - Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
for urun in urunler:
    if int(urun["price"]) <= 5000:
        print(urun["name"])




# DEF FONKSİYONU ÖRNEKLERİ

# Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon yazdırma
def yazdir(kelime, adet):
    print(kelime * adet)

# Fonksiyonu kullanarak kelimeyi 5 kere yazdırma
yazdir('TolAley\n', 5)



# Kendisine gönderilen sınırsız sayıdaki parametreleri bir listeye çeviren bir fonksiyon yazdırma
def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

# Fonksiyonu kullanarak parametreleri bir listeye çevirme
result = listeyeCevir(10, 20, 30, 'Hello')
print(result)



# Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon
def asalSayi(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

# Kullanıcıdan alınan aralıktaki asal sayıları bulma
sayi1 = int(input('Sayı 1: '))
sayi2 = int(input('Sayı 2: '))
asalSayi(sayi1, sayi2)



# Kendisine gönderilen sayının tam bölenlerini bulma
def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2, sayi):
        if sayi % i == 0:
            tamBolenler.append(i)
    return tamBolenler

# Fonksiyonu kullanarak bir sayının tam bölenlerini bulma
print(tamBolenleriBul(20))
