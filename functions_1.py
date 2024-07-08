# Python'da Fonksiyonlar

# Fonksiyonlar, belirli bir görevi yerine getirmek için tanımlanan kod bloklarıdır.
# Fonksiyonlar kodun tekrar kullanılabilirliğini sağlar ve kodun daha okunabilir olmasını sağlar.



# 1. Basit Bir Fonksiyon Tanımlama ve Çağırma
def merhaba_de():
    """
    Bu fonksiyon ekrana 'Merhaba, Dünya!' yazdırır.
    """
    print("Merhaba, Dünya!")

# Fonksiyonu çağırarak kullanabiliriz
merhaba_de()




# 2. Parametre Alan Fonksiyonlar
def selamla(isim):
    """
    Bu fonksiyon bir isim parametresi alır ve o ismi kullanarak selam verir.
    """
    print(f"Merhaba, {isim}!")

# Parametre ile fonksiyonu çağırma
selamla("Aley Kaya")




# 3. Geriye Değer Döndüren Fonksiyonlar
def topla(a, b):
    """
    Bu fonksiyon iki sayı alır ve bu sayıların toplamını geri döner.
    """
    return a + b

# Fonksiyonun döndürdüğü değeri bir değişkende saklayabiliriz
sonuc = topla(3, 5)
print(f"Toplam: {sonuc}")




# 4. Varsayılan Değerli Parametreler
def selamla_mesaj(isim, mesaj="Merhaba"):
    """
    Bu fonksiyon bir isim ve isteğe bağlı olarak bir mesaj alır. 
    Mesaj belirtilmezse varsayılan olarak 'Merhaba' kullanılır.
    """
    print(f"{mesaj}, {isim}!")

# Varsayılan mesaj ile fonksiyonu çağırma
selamla_mesaj("Aley Kaya")

# Özel bir mesaj ile fonksiyonu çağırma
selamla_mesaj("Aley Kaya", "Nasılsın")




# 5. Anahtar Kelime (Keyword) Argümanları
def kisi_bilgileri(ad, soyad, yas):
    """
    Bu fonksiyon kişinin adı, soyadı ve yaşını alır ve bu bilgileri ekrana yazdırır.
    """
    print(f"Ad: {ad}, Soyad: {soyad}, Yaş: {yas}")

# Anahtar kelime argümanları ile fonksiyonu çağırma
kisi_bilgileri(ad="Aley", soyad="Kaya", yas=25)




# 6. Esnek Sayıda Parametreler (*args ve **kwargs)
def toplam_bul(*args):
    """
    Bu fonksiyon herhangi bir sayıda sayıyı alır ve bu sayıların toplamını döner.
    """
    return sum(args)

# Birden fazla argüman ile fonksiyonu çağırma
print(f"Toplam: {toplam_bul(1, 2, 3, 4, 5)}")

def kisi_detaylari(**kwargs):
    """
    Bu fonksiyon herhangi bir sayıda anahtar-değer çiftini alır ve bu bilgileri ekrana yazdırır.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Anahtar kelime argümanları ile fonksiyonu çağırma
kisi_detaylari(ad="Aley", soyad="Kaya", yas=25, sehir="İstanbul")




# 7. Lambda Fonksiyonları
# Lambda fonksiyonları küçük, anonim fonksiyonlardır. Genellikle kısa süreli işlemler için kullanılır.
# Lambda fonksiyonu kullanarak iki sayının toplamını bulma
toplam = lambda a, b: a + b
print(f"Lambda Toplam: {toplam(3, 5)}")




# Fonksiyonların temel kullanımları bu şekildedir. Daha karmaşık işlemler için fonksiyonlar birden fazla işlevi yerine getirebilir
# ve başka fonksiyonları da çağırabilir. Fonksiyonlar Python programlamada önemli bir yer tutar ve kodun düzenli olmasını sağlar.
