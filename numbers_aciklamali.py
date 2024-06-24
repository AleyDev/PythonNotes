# Python'da Sayılar: Temel Veri Tipleri ve İşlemler

# Integer (Tamsayı) Örnekleri
# Integer, negatif veya pozitif tam sayıları temsil eder.
x = 10
y = -5

# Integer işlemleri
toplama_tamsayi = x + y  # Toplama
cikarma_tamsayi = x - y  # Çıkarma
carpma_tamsayi = x * y  # Çarpma
bolme_tamsayi = x / y  # Bölme 
tambolme_tamsayi = x // y # Tam Bölme (tam sayı kısmı)
mod_tamsayi = x % y  # Mod (kalan)
us_tamsayi = x ** y # Üs alma

print(f"Tamsayı işlemleri: Toplama={toplama_tamsayi}, Çıkarma={cikarma_tamsayi}, Çarpma={carpma_tamsayi}, Bölme={bolme_tamsayi}, Tam Bölme={tambolme_tamsayi}, Mod={mod_tamsayi}, Üs={us_tamsayi}")

# Float (Ondalıklı Sayı) Örnekleri
# Float, ondalık noktaya sahip sayıları temsil eder.
a = 3.14
b = -2.71

# Float işlemleri
toplama_float = a + b  # Toplama
cikarma_float = a - b  # Çıkarma
carpma_float = a * b  # Çarpma
bolme_float = a / b  # Bölme

print(f"Ondalıklı sayı işlemleri: Toplama={toplama_float}, Çıkarma={cikarma_float}, Çarpma={carpma_float}, Bölme={bolme_float}")

# Complex (Karmaşık Sayı) Örnekleri
# Complex, karmaşık sayıları temsil eder ve 'j' harfi sanal kısmı belirtir.
c = 2 + 3j
d = 1 - 1j

# Complex işlemleri
toplama_kompleks = c + d  # Toplama
cikarma_kompleks = c - d  # Çıkarma
carpma_kompleks = c * d  # Çarpma
bolme_kompleks = c / d  # Bölme

print(f"Karmaşık sayı işlemleri: Toplama={toplama_kompleks}, Çıkarma={cikarma_kompleks}, Çarpma={carpma_kompleks}, Bölme={bolme_kompleks}")

# Python'da bazı yerleşik sayısal fonksiyonlar
mutlak_deger = abs(-10)  # Mutlak değer
us_alma = pow(2, 3)  # Üs alma (2^3)
yuvarlama = round(3.14159, 2)  # Yuvarlama (2 ondalık basamak)

print(f"Yerleşik fonksiyonlar: Mutlak Değer={mutlak_deger}, Üs Alma={us_alma}, Yuvarlama={yuvarlama}")

# Matematiksel işlemler için math modülünün kullanımı
import math

kare_kok = math.sqrt(16)  # Kare kök
dogal_logaritma = math.log(10)  # Doğal logaritma
sinus = math.sin(math.pi / 2)  # Sinüs

print(f"Math modülü ile işlemler: Kare Kök={kare_kok}, Doğal Logaritma={dogal_logaritma}, Sinüs={sinus}")

# Sayıların veri tipi kontrolü
print(f"Değişken türleri: x'in türü={type(x)}, a'nın türü={type(a)}, c'nin türü={type(c)}")

# Büyük sayılar ile çalışma
# Python'da int veri tipi sınırsız büyüklükte sayıları temsil edebilir.
cok_buyuk_sayi = 10**100
print(f"Çok büyük sayı: {cok_buyuk_sayi}")

# Bilimsel gösterim (Exponential Notation) kullanımı
bilimsel_gosterim = 1.23e4  # 1.23 x 10^4
print(f"Bilimsel gösterim: {bilimsel_gosterim}")
