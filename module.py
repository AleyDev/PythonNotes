# Python'da Modüller

"""
Modüller, belirli bir işlevi yerine getiren Python kod parçalarıdır. 
Modüller sayesinde kod daha okunabilir, tekrar kullanılabilir ve yönetilebilir hale gelir.
"""



# 1. Modül Nedir?
# Bir modül, bir Python dosyasıdır ve bu dosyada tanımlanan fonksiyonlar, sınıflar ve değişkenler başka Python dosyalarında kullanılabilir. Örneğin, "math" modülü matematiksel işlemler için hazır fonksiyonlar içerir.

import math  # math modülü import ediliyor

# math modülünden pi değerini ve karekök fonksiyonunu kullanmak
print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0



# 2. Kendi Modülünüzü Oluşturma
# Kendi modülünüzü oluşturmak için bir Python dosyası oluşturmanız yeterlidir.
# Örneğin, "mymodule.py" adında bir dosya oluşturulduğunu varsayalım.

# mymodule.py içeriği:
# def merhaba():
#     print("Merhaba, dünya!")
#
# def topla(a, b):
#     return a + b

# Şimdi, bu modülü başka bir Python dosyasından nasıl kullanacağımıza bakalım.

# başka_dosya.py içeriği:
import mymodule  # "mymodule.py" dosyasındaki fonksiyonlar import ediliyor

# mymodule içindeki fonksiyonları kullanmak
mymodule.merhaba()  # Merhaba, dünya!
print(mymodule.topla(5, 3))  # 8



# 3. Modülden Belirli Fonksiyonları veya Değişkenleri İçe Aktarma
# Bazen bir modülden sadece belirli fonksiyonları veya değişkenleri kullanmak istenebilir.
# Bu durumda "from" anahtar kelimesi kullanılabilir.

from math import pi, sqrt  # math modülünden sadece pi ve sqrt fonksiyonları import ediliyor

print(pi)      # 3.141592653589793
print(sqrt(25))  # 5.0



# 4. Modülleri Yeniden Adlandırma (Alias)
# Modül isimleri uzun veya karmaşık olduğunda, onları daha kısa bir isimle yeniden adlandırmak mümkündür.

import math as m  # math modülü "m" olarak yeniden adlandırılıyor

print(m.pi)      # 3.141592653589793
print(m.sqrt(36))  # 6.0



# 5. Standart Kütüphane Modülleri
# Python, birçok kullanışlı modül içeren geniş bir standart kütüphaneye sahiptir. Bu modüller çeşitli işlevler için hazır fonksiyonlar sağlar.

import datetime  # datetime modülü kullanılarak tarih ve saat işlemleri yapılabilir

# Şu anki tarih ve saat
now = datetime.datetime.now()
print(now)  # Örneğin: 2024-07-15 12:34:56.789012



# 6. Özel Modüller ve Üçüncü Taraf Kütüphaneler
# Python, standart kütüphanesinin dışında birçok üçüncü taraf kütüphane ve modül sunar.
# Bu kütüphaneler, belirli ihtiyaçları karşılamak için ek işlevsellik sağlar.

# Örneğin, "requests" modülü HTTP istekleri yapmayı kolaylaştırır.
# Bu kütüphaneyi kullanmak için önce yüklemek gerekir: pip install requests

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())  # API yanıtını JSON formatında döndürür



# 7. __name__ ve __main__ Değişkeni
# Python'da her modülün kendi özel bir __name__ değişkeni vardır. Bir dosya doğrudan çalıştırıldığında, __name__ değeri "__main__" olarak ayarlanır. Bu, bir dosyanın doğrudan mı yoksa başka bir dosya tarafından mı çalıştırıldığını anlamak için kullanılabilir.

# mymodule.py dosyasını bu şekilde güncelleyin:
# def merhaba():
#     print("Merhaba, dünya!")
#
# def topla(a, b):
#     return a + b
#
# if __name__ == "__main__":
#     # Bu blok sadece mymodule.py doğrudan çalıştırıldığında çalışır
#     print("mymodule doğrudan çalıştırıldı.")
#     merhaba()
#     print(topla(10, 20))

# başka_dosya.py içeriği:
# import mymodule

# mymodule.merhaba()
# print(mymodule.topla(3, 7))

# Başka_dosya.py çalıştırıldığında "mymodule doğrudan çalıştırıldı." mesajı yazılmaz.

# Örnek Proje: Basit Hesap Makinesi Modülü

# hesap_makinesi.py dosyası:
# def topla(a, b):
#     return a + b
#
# def cikar(a, b):
#     return a - b
#
# def carp(a, b):
#     return a * b
#
# def bol(a, b):
#     if b == 0:
#         return "Hata: Bölme sıfıra yapılamaz"
#     return a / b

# main.py dosyası:
import hesap_makinesi as hm

print(hm.topla(10, 5))     # 15
print(hm.cikar(10, 5))     # 5
print(hm.carp(10, 5))      # 50
print(hm.bol(10, 5))       # 2.0
print(hm.bol(10, 0))       # Hata: Bölme sıfıra yapılamaz



# Modüllerin temel kullanımları bu şekildedir. Daha karmaşık işlemler için modüller birden fazla işlevi yerine getirebilir ve başka modülleri de çağırabilir. Modüller Python programlamada önemli bir yer tutar ve kodun düzenli olmasını sağlar.
