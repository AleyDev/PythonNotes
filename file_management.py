# Python'da Dosya Yönetimi

# Python'da dosya yönetimi, dosya açma, okuma, yazma ve kapama işlemlerini içerir.
# Bu işlemler genellikle `open`, `read`, `write` ve `close` metotları kullanılarak yapılır.

# 1. Dosya Açma ve Kapama
# `open()` fonksiyonu, bir dosyayı açmak için kullanılır.
# `open` fonksiyonu iki ana argüman alır: dosya adı ve dosya modu.
# Dosyayı açtıktan sonra kapatmak için close() fonksiyonu kullanılır.
# Dosya açma modları:
# 'r' : Okuma modu (varsayılan). Dosya mevcut değilse hata verir.
# 'w' : Yazma modu. Dosya yoksa oluşturur, varsa içeriğini siler.
# 'a' : Ekleme modu. Dosya yoksa oluşturur, varsa sonuna ekler.
# 'b' : İkili (binary) mod. Örneğin 'rb' (okuma için ikili mod).
# 't' : Metin (text) modu (varsayılan). Örneğin 'rt' (okuma için metin modu).
# 'x' : Yalnızca yeni dosya oluşturma modu. Dosya varsa hata verir.

"""Dosya Oluşturma
Dosya oluşturmak için 'w' (yazma) veya 'a' (ekleme) modunda açabiliriz.
Eğer dosya yoksa, bu modlarda açıldığında dosya otomatik olarak oluşturulur."""

# Örnek: Bir dosyayı okuma modunda açma
file = open("example.txt", "r") # "example.txt" adlı dosyayı okuma modunda açar
file = open("example.txt", "w")  # 'example.txt' adlı dosyayı yazma modunda açar
file.write("Merhaba, Dünya!")  # Dosyaya veri yazar

# Dosyayı kapatma
file.close()  # Dosyayı kapatır



# 2. Dosya Okuma
# `read` metodu, dosyadaki tüm içeriği okumak için kullanılır.
# `readline` metodu, dosyadan bir satır okumak için kullanılır.
# `readlines` metodu, dosyadaki tüm satırları liste olarak okumak için kullanılır.

# Dosyadan tüm içeriği okuma read()
content = file.read()
print(content)  # Dosyanın içeriğini yazdırır

# Dosyadan bir satır okuma (readline)
with open("example.txt", "r") as file:
    first_line = file.readline()  # İlk satırı okur
    print(first_line)  # Çıktı: Satır 1

# Dosyadaki tüm satırları okuma (readlines)
with open("example.txt", "r") as file:
    all_lines = file.readlines()  # Tüm satırları okur ve liste olarak döner
    print(all_lines)  # Çıktı: ['Satır 1\n', 'Satır 2\n', 'Satır 3\n']



# 3. Dosyaya Yazma - write() ve writelines()
# `write() ve writelines()` metodu, dosyaya veri yazmak için kullanılır.
# Eğer dosya yazma modunda ('w') açıldıysa, mevcut dosya silinir ve yeni bir dosya oluşturulur.
# Eğer dosya ekleme modunda ('a') açıldıysa, mevcut dosyaya veri eklenir.

# Örnek: Dosyaya yazma write()
file = open("example.txt", "w")
file.write("Merhaba, dünya!")
file.close()

# writelines() örneği
lines = ["Satır 1\n", "Satır 2\n", "Satır 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)  # Birden fazla satırı dosyaya yazar



# 4. Dosyaya Ekleme
# `a` modu ile açılan dosyaya veri eklenir, mevcut veri korunur.

# Örnek: Dosyaya ekleme
file = open("example.txt", "a")
file.write("\nYeni satır.")
file.close()

# Ekleme örneği
with open("example.txt", "a") as file:
    file.write("Yeni bir satır ekliyorum.\n")  # Dosyanın sonuna yeni bir satır ekler

    

# 5. `with` Anahtar Kelimesi
# `with` anahtar kelimesi, dosya yönetiminde yaygın olarak kullanılır çünkü dosya işiniz bittiğinde otomatik olarak dosyayı kapatır.
# `with` bloğu sona erdiğinde, dosya otomatik olarak kapanır.

# Örnek: `with` kullanarak dosya açma ve okuma- Bu yöntemle dosya otomatik olarak kapanır
with open("example.txt", "r") as file:
    content = file.read() # Dosyanın içeriğini okur
    print(content)  # Dosyanın içeriğini yazdırır

# Örnek: `with` kullanarak dosyaya yazma
with open("example.txt", "w") as file:
    file.write("Merhaba, dünya!") # Dosyaya veri yazar
    file.write("\nYeni satır.")



# 6. Dosya Modları ve Diğer Özellikler
# Dosya modları birleştirilebilir, örneğin 'rb' modu, ikili okuma modudur.
# `seek` metodu, dosya içindeki bir konuma gitmek için kullanılır.
# `tell` metodu, dosya içindeki mevcut konumu döndürür.

# Örnek: Dosya modları ve diğer özellikler
with open("example.txt", "rb") as file:
    content = file.read() # Dosya içeriğini okur
    print(content)  # İkili dosya içeriğini yazdırır



# 7. Dosya Varlığını Kontrol Etme
# `os.path.exists` fonksiyonu, dosyanın var olup olmadığını kontrol eder.

import os

# Örnek: Dosya varlığını kontrol etme
if os.path.exists("example.txt"):
    print("Dosya mevcut.")
else:
    print("Dosya mevcut değil.")



# 8. Dosya Silme
# `os.remove` fonksiyonu, bir dosyayı silmek için kullanılır.

# Örnek: Dosya silme
if os.path.exists("example.txt"):
    os.remove("example.txt") # Dosyayı siler.
    print("Dosya silindi.")
else:
    print("Silinecek dosya mevcut değil.")


# Dosya Güncelleme
# Dosya güncelleme, mevcut dosyanın belirli bir kısmını değiştirmek anlamına gelir.
# Bunun için dosya içeriğini okur, gerekli değişiklikleri yapar ve ardından dosyaya yeniden yazarız.

# Örnek: Dosya güncelleme
with open("example.txt", "r") as file:
    lines = file.readlines()  # Dosyanın tüm satırlarını okur

# Belirli bir satırı güncelleme
lines[1] = "Güncellenmiş satır 2\n"

with open("example.txt", "w") as file:
    file.writelines(lines)  # Güncellenmiş içeriği dosyaya yazar

# Güncellenmiş dosya içeriğini okuma
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Çıktı: Satır 1\nGüncellenmiş satır 2\nSatır 3\nYeni bir satır ekliyorum.\n
