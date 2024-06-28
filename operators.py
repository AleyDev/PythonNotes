# Python Operatörleri

# 1. Aritmetik Operatörler

# Toplama Operatörü (+): İki sayıyı toplar.
a = 10
b = 5
toplam = a + b
print("Toplama:", toplam)  # Çıktı: 15

# Çıkarma Operatörü (-): Birinci sayıdan ikinci sayıyı çıkarır.
cikarma = a - b
print("Çıkarma:", cikarma)  # Çıktı: 5

# Çarpma Operatörü (*): İki sayıyı çarpar.
carpma = a * b
print("Çarpma:", carpma)  # Çıktı: 50

# Bölme Operatörü (/): Birinci sayıyı ikinci sayıya böler.
bolme = a / b
print("Bölme:", bolme)  # Çıktı: 2.0

# Tam Bölme Operatörü (//): Birinci sayıyı ikinci sayıya böler ve sonucu tam sayı olarak döner.
tam_bolme = a // b
print("Tam Bölme:", tam_bolme)  # Çıktı: 2

# Mod Alma Operatörü (%): Birinci sayının ikinci sayıya bölümünden kalan değeri verir.
mod = a % b
print("Mod Alma:", mod)  # Çıktı: 0

# Üs Alma Operatörü (**): Birinci sayıyı ikinci sayının kuvvetine yükseltir.
us = a ** b
print("Üs Alma:", us)  # Çıktı: 100000



# 2. Atama Operatörleri

# Atama Operatörü (=): Sağdaki değeri soldaki değişkene atar.
a = 10
print("Atama:", a)  # Çıktı: 10

# Toplama ve Atama Operatörü (+=): Sağdaki değeri soldaki değişkene ekleyip sonucu soldaki değişkene atar.
a += 5
print("Toplama ve Atama:", a)  # Çıktı: 15

# Çıkarma ve Atama Operatörü (-=): Sağdaki değeri soldaki değişkenden çıkarıp sonucu soldaki değişkene atar.
a -= 3
print("Çıkarma ve Atama:", a)  # Çıktı: 12

# Çarpma ve Atama Operatörü (*=): Sağdaki değeri soldaki değişkenle çarpıp sonucu soldaki değişkene atar.
a *= 2
print("Çarpma ve Atama:", a)  # Çıktı: 24

# Bölme ve Atama Operatörü (/=): Sağdaki değeri soldaki değişkene böler ve sonucu soldaki değişkene atar.
a /= 4
print("Bölme ve Atama:", a)  # Çıktı: 6.0

# Tam Bölme ve Atama Operatörü (//=): Sağdaki değeri soldaki değişkene böler ve sonucu tam sayı olarak soldaki değişkene atar.
a //= 2
print("Tam Bölme ve Atama:", a)  # Çıktı: 3.0

# Mod Alma ve Atama Operatörü (%=): Sağdaki değeri soldaki değişkene böler ve kalan değeri soldaki değişkene atar.
a %= 2
print("Mod Alma ve Atama:", a)  # Çıktı: 1

# Üs Alma ve Atama Operatörü (**=): Sağdaki değeri soldaki değişkenin kuvveti olarak alıp sonucu soldaki değişkene atar.
a **= 3
print("Üs Alma ve Atama:", a)  # Çıktı: 1



# 3. Karşılaştırma Operatörleri

# Eşitlik Operatörü (==): İki değeri karşılaştırır ve eşitse True döner.
print("Eşit mi:", a == 1)  # Çıktı: True

# Eşit Değil Operatörü (!=): İki değeri karşılaştırır ve eşit değilse True döner.
print("Eşit Değil mi:", a != 1)  # Çıktı: False

# Büyüktür Operatörü (>): Birinci değer ikinci değerden büyükse True döner.
print("Büyük mü:", a > 1)  # Çıktı: False

# Küçüktür Operatörü (<): Birinci değer ikinci değerden küçükse True döner.
print("Küçük mü:", a < 1)  # Çıktı: False

# Büyük Eşittir Operatörü (>=): Birinci değer ikinci değerden büyük veya eşitse True döner.
print("Büyük veya Eşit mi:", a >= 1)  # Çıktı: True

# Küçük Eşittir Operatörü (<=): Birinci değer ikinci değerden küçük veya eşitse True döner.
print("Küçük veya Eşit mi:", a <= 1)  # Çıktı: True



# 4. Mantıksal Operatörler

# Ve Operatörü (and): Her iki koşul da doğruysa True döner.
x = True
y = False
print("Ve Operatörü:", x and y)  # Çıktı: False

# Veya Operatörü (or): Koşullardan biri doğruysa True döner.
print("Veya Operatörü:", x or y)  # Çıktı: True

# Değil Operatörü (not): Koşulun tersini döner.
print("Değil Operatörü:", not x)  # Çıktı: False



# -------------------------------------------------------------------
# Sık kullanılmıyor olsa da bilinmesi gereken diğer operatörler:

# 5. Bit Düzeyinde Operatörler (Bitwise Operators)

# Bit düzeyinde işlemler sadece integer tipinde sayılarla yapılır.
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Ve Operatörü (&): İki sayının bit düzeyinde ve işlemini yapar.
print("Bit Düzeyinde Ve:", a & b)  # Çıktı: 0

# Veya Operatörü (|): İki sayının bit düzeyinde veya işlemini yapar.
print("Bit Düzeyinde Veya:", a | b)  # Çıktı: 14

# XOR Operatörü (^): İki sayının bit düzeyinde XOR işlemini yapar.
print("Bit Düzeyinde XOR:", a ^ b)  # Çıktı: 14

# Değil Operatörü (~): Sayının bit düzeyinde tersini alır.
print("Bit Düzeyinde Değil:", ~a)  # Çıktı: -11

# Sol Kaydırma Operatörü (<<): Sayının bitlerini sola kaydırır.
print("Sol Kaydırma:", a << 1)  # Çıktı: 20

# Sağ Kaydırma Operatörü (>>): Sayının bitlerini sağa kaydırır.
print("Sağ Kaydırma:", a >> 1)  # Çıktı: 5



# 6. Üyelik Operatörleri

# İn Operatörü (in): Bir değerin bir koleksiyonda olup olmadığını kontrol eder.
liste = [1, 2, 3]
print("İçinde mi:", 2 in liste)  # Çıktı: True

# Değil İn Operatörü (not in): Bir değerin bir koleksiyonda olup olmadığını kontrol eder.
print("İçinde değil mi:", 4 not in liste)  # Çıktı: True



# 7. Kimlik Operatörleri

# Kimlik Operatörü (is): İki nesnenin aynı nesne olup olmadığını kontrol eder.
a = [1, 2, 3]
b = a
print("Aynı nesne mi:", a is b)  # Çıktı: True

# Kimlik Değil Operatörü (is not): İki nesnenin aynı nesne olup olmadığını kontrol eder.
c = a[:]
print("Aynı nesne değil mi:", a is not c)  # Çıktı: True