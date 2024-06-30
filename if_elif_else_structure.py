# Python'da if-elif-else Yapısı: Kontrol Akışı

# if-elif-else yapısı, koşullu ifadeleri değerlendirerek farklı kod bloklarının çalışmasını sağlar.
# Bir koşul True (doğru) ise, ilgili blok çalışır. Birden fazla koşul varsa, sırayla kontrol edilir ve ilk True olan blok çalıştırılır.


# Basit if-elif-else Yapısı
a = 10
b = 20


# if ifadesi: Eğer koşul True ise if bloğu çalışır.
if a < b:
    print("a, b'den küçüktür.")  # Bu koşul doğru olduğu için çalışacak.
# elif ifadesi: İlk koşul False ise elif bloğu kontrol edilir.
elif a == b:
    print("a ve b eşittir.")  # Bu koşul sağlanmadığı için çalışmayacak.
# else ifadesi: Yukarıdaki koşulların hiçbiri True değilse else bloğu çalışır.
else:
    print("a, b'den büyük veya eşittir.")  # Bu koşul da çalışmayacak çünkü a < b.



# Daha karmaşık if-elif-else Yapısı
x = 50

if x > 0:
    print("x pozitif bir sayıdır.")  # Bu koşul doğru olduğu için çalışacak.
elif x == 0:
    print("x sıfırdır.")  # Bu koşul sağlanmadığı için çalışmayacak.
else:
    print("x negatif bir sayıdır.")  # Bu koşul da çalışmayacak çünkü x > 0.



# Birden fazla elif ifadesi
notu = 85

if notu >= 90:
    print("Notunuz: A")  # Bu koşul sağlanmadığı için çalışmayacak.
elif notu >= 80:
    print("Notunuz: B")  # Bu koşul doğru olduğu için çalışacak.
elif notu >= 70:
    print("Notunuz: C")  # Bu koşul da çalışmayacak çünkü önceki koşul sağlandı.
elif notu >= 60:
    print("Notunuz: D")  # Bu koşul da çalışmayacak çünkü önceki koşullar sağlandı.
else:
    print("Notunuz: F")  # Bu koşul da çalışmayacak çünkü önceki koşullar sağlandı.



# İç içe if-elif-else Yapısı
yas = 25
gelir = 5000

if yas > 18:
    if gelir > 3000:
        print("Kredi alabilirsiniz.")  # Bu koşul doğru olduğu için çalışacak.
    else:
        print("Geliriniz yeterli değil.")  # Bu koşul da çalışmayacak çünkü önceki koşul sağlandı.
else:
    print("Yaşınız kredi almak için yeterli değil.")  # Bu koşul da çalışmayacak çünkü yas > 18 koşulu sağlandı.



# Tek satırlık if-else (Ternary) Operatörü

# Ternary operatörü, tek satırda if-else yapısını kullanmanızı sağlar.
yas = 20
yetiskin_mi = "Evet" if yas >= 18 else "Hayır"
print("Yetişkin misiniz?", yetiskin_mi)  # Çıktı: Yetişkin misiniz? Evet



# ---------------------------------------------------------------------------

# Örnek 1: Mevsim Belirleme

ay = "Mart"

if ay == "Mart" or ay == "Nisan" or ay == "Mayıs":
    print("Bahar mevsimi")
elif ay == "Haziran" or ay == "Temmuz" or ay == "Ağustos":
    print("Yaz mevsimi")
elif ay == "Eylül" or ay == "Ekim" or ay == "Kasım":
    print("Sonbahar mevsimi")
elif ay == "Aralık" or ay == "Ocak" or ay == "Şubat":
    print("Kış mevsimi")
else:
    print("Geçersiz ay")
# Çıktı: Bahar mevsimi (çünkü ay değişkeni "Mart")



# Örnek 2: Not Hesaplama

ogrNotu = 75

if ogrNotu >= 90:
    print("Notunuz: A")
elif ogrNotu >= 80:
    print("Notunuz: B")
elif ogrNotu >= 70:
    print("Notunuz: C")
elif ogrNotu >= 60:
    print("Notunuz: D")
else:
    print("Notunuz: F")

# Çıktı: Notunuz: C (çünkü notu değişkeni 75)




""""
if-elif-else Yapısının Avantajları
1. Koşullu ifadelerle karar verme süreçlerini yönetir.
2. Kodun okunabilirliğini ve anlaşılabilirliğini artırır.
3. Farklı koşullara göre farklı kod bloklarının çalıştırılmasını sağlar.


if-elif-else Kullanım Alanları
1. Kullanıcı girdilerine göre farklı işlemler yapma.
2. Farklı koşullara göre farklı işlemler gerçekleştirme.
3. Karar verme süreçlerinin yönetilmesi gereken her türlü durumda.
"""