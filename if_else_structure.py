# Python'da if-else Yapısı: Kontrol Akışı

# if-else Nedir?
# if-else yapısı, koşullu ifadeleri değerlendirerek farklı kod bloklarının çalışmasını sağlar.
# if ifadesi True (doğru) ise, ilgili kod bloğu çalışır. Aksi halde, else bloğu çalışır.



# Basit if-else yapısı
a = 10
b = 20



# if ifadesi: Eğer koşul True ise, if bloğu çalışır.
if a < b:
    print("a, b'den küçüktür.")  # Çıktı: a, b'den küçüktür.
else:
    print("a, b'den büyük veya eşittir.")



# elif ifadesi (else if): Birden fazla koşul kontrolü yapmak için kullanılır.
# İlk koşul False ise, elif bloğu kontrol edilir.
if a > b:
    print("a, b'den büyüktür.")
elif a == b:
    print("a, b'ye eşittir.")
else:
    print("a, b'den küçüktür.")  # Çıktı: a, b'den küçüktür.



# Birden fazla elif ifadesi kullanımı
x = 15

if x < 10:
    print("x, 10'dan küçüktür.")
elif x < 20:
    print("x, 10 ile 20 arasında.")  # Çıktı: x, 10 ile 20 arasında.
elif x < 30:
    print("x, 20 ile 30 arasında.")
else:
    print("x, 30 veya daha büyüktür.")



# İç içe if-else (nested if-else) kullanımı
y = 25

if y > 10:
    print("y, 10'dan büyüktür.")  # Çıktı: y, 10'dan büyüktür.
    
    if y > 20:
        print("y, 20'den de büyüktür.")  # Çıktı: y, 20'den de büyüktür.
    else:
        print("y, 20'den küçüktür.")
else:
    print("y, 10'dan küçüktür.")



# Tek satırda if-else ifadesi (ternary operator)
# Ternary operator, kısa if-else ifadeleri için kullanılır.
z = 5
sonuc = "Pozitif" if z > 0 else "Negatif veya Sıfır"
print("Sonuç:", sonuc)  # Çıktı: Sonuç: Pozitif



# Örnek: Kullanıcıdan alınan yaş bilgisine göre sınıflandırma
yas = int(input("Yaşınızı girin: "))

if yas < 18:
    print("Reşit değilsiniz.")
elif 18 <= yas < 65:
    print("Çalışma çağında bir yetişkinsiniz.")
else:
    print("Emeklilik yaşındasınız.")



# if-else ile mantıksal operatörlerin kullanımı
a = 30
b = 40
c = 50

if a < b and b < c:
    print("a, b'den ve b de c'den küçüktür.")  # Çıktı: a, b'den ve b de c'den küçüktür.
else:
    print("Koşul sağlanmadı.")

if a > b or b < c:
    print("a, b'den büyük veya b, c'den küçüktür.")  # Çıktı: a, b'den büyük veya b, c'den küçüktür.
else:
    print("Hiçbir koşul sağlanmadı.")



# if-else ile karşılaştırma operatörlerinin kullanımı
m = 100
n = 200

if m != n:
    print("m ve n eşit değil.")  # Çıktı: m ve n eşit değil.
else:
    print("m ve n eşit.")



# if-else ile üyelik operatörlerinin kullanımı
liste = [1, 2, 3, 4, 5]

if 3 in liste:
    print("3, liste içinde mevcut.")  # Çıktı: 3, liste içinde mevcut.
else:
    print("3, liste içinde mevcut değil.")



# if-else ile kimlik operatörlerinin kullanımı
x = [1, 2, 3]
y = x

if x is y:
    print("x ve y aynı nesnedir.")  # Çıktı: x ve y aynı nesnedir.
else:
    print("x ve y aynı nesne değildir.")

z = x[:]

if x is not z:
    print("x ve z aynı nesne değildir.")  # Çıktı: x ve z aynı nesne değildir.
else:
    print("x ve z aynı nesnedir.")



# -----------------------------------------------------------

# Örnek 1: Kullanıcı Girişi Doğrulama

username = "user1"
password = "password123"

input_username = input("Kullanıcı adınızı girin: ")
input_password = input("Şifrenizi girin: ")

# if-else ifadesi: Kullanıcı adı ve şifre doğruluğunu kontrol eder.
if input_username == username and input_password == password:
    print("Giriş başarılı.")  # Çıktı: Giriş başarılı.
else:
    print("Giriş başarısız.")  # Çıktı: Giriş başarısız.



# Örnek 2: Not Kontrolü

vize = float(input("Vize notunuzu girin: "))
final = float(input("Final notunuzu girin: "))

ortalama = (vize * 0.4) + (final * 0.6)

# if-else ifadesi: Ortalama not 60 ve üzeri ise geçer, değilse kalır.
if ortalama >= 60:
    print("Geçtiniz.")  # Çıktı: Geçtiniz.
else:
    print("Kaldınız.")  # Çıktı: Kaldınız.