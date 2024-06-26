# Python'da Dictionary (Sözlük): Temel Veri Türleri ve İşlemler

# Dictionary Nedir?
# Dictionary (sözlük), anahtar-değer (key-value) çiftlerini saklamak için kullanılan bir veri yapısıdır. 
# Anahtarlar benzersiz olmalıdır, fakat değerler aynı olabilir.
# Dictionary'ler süslü parantez {} kullanılarak tanımlanır.


# Python'da Dictionary Tanımlama
sozluk1 = {
    "isim": "Aley",
    "yas": 24,
    "sehir": "İstanbul"
}
print("Sözlük 1:", sozluk1)

sozluk2 = {
    "marka": "Ford",
    "model": "Mustang",
    "yil": 1964
}
print("Sözlük 2:", sozluk2)



# Boş bir dictionary tanımlama
bos_sozluk = {}
print("Boş Sözlük:", bos_sozluk)



# Dictionary Elemanlarına Erişim
# Anahtarlar kullanılarak değerlerine erişilebilir.
isim = sozluk1["isim"]
yas = sozluk1["yas"]
print("İsim:", isim)
print("Yaş:", yas)


# get() metodu ile elemanlara erişim
sehir = sozluk1.get("sehir")
print("Şehir:", sehir)



# Dictionary Elemanlarını Güncelleme
sozluk1["yas"] = 24
print("Güncellenmiş Sözlük 1:", sozluk1)



# Yeni anahtar-değer çifti ekleme
sozluk1["meslek"] = "Yazılım Geliştirici"
print("Meslek Eklenmiş Sözlük 1:", sozluk1)



# Dictionary'den Eleman Silme
# pop() metodu: Belirtilen anahtarı ve ona ait değeri siler
yas = sozluk1.pop("yas")
print("Yaşı Silinmiş Sözlük 1:", sozluk1)
print("Silinen Yaş:", yas)

# del ifadesi: Belirtilen anahtarı ve ona ait değeri siler
del sozluk1["sehir"]
print("Şehir Silinmiş Sözlük 1:", sozluk1)

# clear() metodu: Sözlükteki tüm anahtar-değer çiftlerini siler
sozluk1.clear()
print("Tüm Elemanları Silinmiş Sözlük 1:", sozluk1)



# Dictionary Uzunluğu (Eleman Sayısı)
sozluk2_uzunluk = len(sozluk2)
print("Sözlük 2'nin Uzunluğu:", sozluk2_uzunluk)



# Tüm Anahtarlar, Değerler ve Anahtar-Değer Çiftleri
# keys() metodu: Sözlükteki tüm anahtarları döner
anahtarlar = sozluk2.keys()
print("Sözlük 2'nin Anahtarları:", anahtarlar)

# values() metodu: Sözlükteki tüm değerleri döner
degerler = sozluk2.values()
print("Sözlük 2'nin Değerleri:", degerler)

# items() metodu: Sözlükteki tüm anahtar-değer çiftlerini döner
anahtar_degerler = sozluk2.items()
print("Sözlük 2'nin Anahtar-Değer Çiftleri:", anahtar_degerler)



# Dictionary Kopyalama
# copy() metodu: Sözlüğü kopyalar
sozluk2_kopya = sozluk2.copy()
print("Kopyalanmış Sözlük 2:", sozluk2_kopya)



# Birleşik (Nested) Dictionary
# İç içe sözlükler oluşturulabilir
birlesik_sozluk = {
    "araba1": {
        "marka": "Ford",
        "model": "Mustang",
        "yil": 1964
    },
    "araba2": {
        "marka": "BMW",
        "model": "X5",
        "yil": 2020
    }
}
print("Birleşik Sözlük:", birlesik_sozluk)



# Birleşik Dictionary Elemanlarına Erişim
araba1_model = birlesik_sozluk["araba1"]["model"]
print("Araba 1 Modeli:", araba1_model)



# Dictionary ile Değişken Atama (Unpacking)
sozluk3 = {"bir": 1, "iki": 2, "uc": 3}
a, b, c = sozluk3.values()
print("a:", a, "b:", b, "c:", c)



# Dictionary'nin Avantajları:
# 1. Anahtar-değer yapısı ile verilerin hızlıca erişilebilmesi.
# 2. Farklı veri türlerinin bir arada tutulabilmesi.
# 3. Anahtarlar immutable olduğu için veri güvenliği sağlar.


# Dictionary Kullanım Alanları
# 1. Veritabanı kayıtları, kullanıcı bilgileri gibi yapıların saklanmasında.
# 2. JSON verilerinin temsil edilmesinde.
# 3. Hızlı arama ve veri erişimi gerektiren durumlarda.



# Dictionary Kullanım Örnekleri

# 1. Kullanıcı Bilgileri Saklama
kullanici = {
    "kullanici_adi": "aleydev",
    "sifre": "password123",
    "email": "aleydev@example.com"
}
print("Kullanıcı Bilgileri:", kullanici)



# 2. JSON Verisi Temsil Etme
json_verisi = {
    "isim": "TU",
    "yas": 26,
    "adres": {
        "sehir": "İstanbul",
        "posta_kodu": 34220
    }
}
print("JSON Verisi:", json_verisi)



# Öğrenci Bilgileri Örneği: Farklı Yöntemlerle Sözlük Güncelleme
ogrenci = {}

number = input("Öğrenci Numarası: ")
name = input("Ad: ")
surname = input("Soyad: ")
phone = input("Telefon numarası: ")

# Yöntem 1: Anahtar-değer çiftlerini doğrudan atama
ogrenci[number] = {
    "ad": name,
    "soyad": surname,
    "telefon": phone
}

# Yöntem 2: update() metodu ile sözlüğü güncelleme
ogrenci.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print("Öğrenci Bilgileri:", ogrenci)



"""-----------------------------------------------------------------"""


# Örnek: Rolls-Royce Spectre Model Bilgileri
rolls_royce_spectre = {
    "marka": "Rolls-Royce",
    "model": "Spectre",
    "yil": 2024,
    "motor": "Elektrikli",
    "guc": "577 hp",
    "maksimum_hiz": "250 km/s",
    "fiyat": "Yaklaşık 400,000 USD"
}
print("Rolls-Royce Spectre Model Bilgileri:", rolls_royce_spectre)

# Dictionary Elemanlarına Erişim
marka = rolls_royce_spectre["marka"]
model = rolls_royce_spectre["model"]
yil = rolls_royce_spectre["yil"]
motor = rolls_royce_spectre["motor"]

print("Marka:", marka)
print("Model:", model)
print("Yıl:", yil)
print("Motor:", motor)

# Yeni Bir Anahtar-Değer Çifti Ekleme
rolls_royce_spectre["renk"] = "Siyah"
print("Renk Eklenmiş Rolls-Royce Spectre Model Bilgileri:", rolls_royce_spectre)

# Dictionary Uzunluğu (Eleman Sayısı)
sozluk_uzunluk = len(rolls_royce_spectre)
print("Rolls-Royce Spectre Model Bilgilerinin Eleman Sayısı:", sozluk_uzunluk)

# Tüm Anahtarlar, Değerler ve Anahtar-Değer Çiftleri
anahtarlar = rolls_royce_spectre.keys()
degerler = rolls_royce_spectre.values()
anahtar_degerler = rolls_royce_spectre.items()

print("Rolls-Royce Spectre Modelinin Anahtarları:", anahtarlar)
print("Rolls-Royce Spectre Modelinin Değerleri:", degerler)
print("Rolls-Royce Spectre Modelinin Anahtar-Değer Çiftleri:", anahtar_degerler)
