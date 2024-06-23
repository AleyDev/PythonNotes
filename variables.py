# Değişken Tanımlama Kuralları

# Python'da değişken tanımlama ve kurallarını gösteren örnekler

# 1. Harf veya alt çizgi ile başlama
name = "Aleyna"        # Geçerli
print(name)
_age = 24            # Geçerli
print(_age)
# 1name = "Ky"      # Geçersiz: rakamla başlayamaz

# 2. Alfanümerik karakterler ve alt çizgi kullanma
user_name = "Alkaya"  # Geçerli
print(user_name)
user123 = "AleyDev"      # Geçerli
print(user123)
# user-name = "aleydev"  # Geçersiz: tire (-) kullanılamaz
# user name = "aleydev"  # Geçersiz: boşluk kullanılamaz

# 3. Python anahtar kelimeleri kullanılamaz
# class = "First"    # Geçersiz: 'class' anahtar kelimesi

# 4. Büyük/küçük harf duyarlılığı
var = 5              # Geçerli
Var = 10             # Geçerli ve farklı bir değişken

# 5. Değişkenlerin değerlerini değiştirme
x = 100              # Geçerli
print(x)             # Çıktı: 100
x = 200              # Geçerli
print(x)             # Çıktı: 200

# Farklı veri türleri ile değişkenler
integer_var = 10            # Tamsayı
float_var = 20.5            # Ondalıklı sayı
string_var = "Hello World"  # Metinsel
boolean_var = True          # Mantıksal (Doğru/Yanlış)
isStudent = False

# Bir değişkene birden fazla kez atama yapılabilir
number = 5
number = number + 10
print(number)  # Çıktı: 15

# Örnek: Değişken isimlendirme kurallarına uyan bir kod- String birleştirme işlemi
first_name = "Aleyna"
last_name = "Ky"
full_name = first_name + " " + last_name
print(full_name)  # Çıktı: Aleyna Ky

# Örnek: Değişkenlerde büyük/küçük harf duyarlılığı
temperature = 25
Temperature = 30
print(temperature)  # Çıktı: 25
print(Temperature)  # Çıktı: 30
