# Python'da Listeler: Temel Veri Türleri ve İşlemler

# Liste Nedir?
# Liste, Python'da birden fazla öğeyi bir arada saklamak için kullanılan bir veri yapısıdır. 
# Listeler, sıralı ve değiştirilebilir (mutable) veri tipleridir. Farklı veri tiplerini bir arada barındırabilirler.
# Listeler, köşeli parantez [] kullanılarak tanımlanır.


# Python'da Liste Tanımlama
liste1 = [1, 2, 3, 4, 5]  # Tam sayılardan oluşan bir liste
liste2 = ["ananas", "mango", "kivi"]  # Metinlerden (string) oluşan bir liste
liste3 = [1, "ananas", 3.5, True]  # Farklı veri tiplerinden oluşan bir liste
liste4 = []  # Boş bir liste

print("Liste 1:", liste1)
print("Liste 2:", liste2)
print("Liste 3:", liste3)
print("Boş Liste:", liste4)



# Stringi Listeye Dönüştürme -1:  Harf harf yazdırır
string = "Python"
string_to_list = list(string)
print("String'den Listeye Dönüştürülmüş Hali:", string_to_list)

# Stringi Listeye Dönüştürme - 2: İfadeyi liste içerisinde yazdırır
string = "Python"
string_to_list = [string]
print("String'den Listeye Dönüştürülmüş Hali:", string_to_list)



# Stringi Belirli Bir Ayırıcıya Göre Bölme
str = "Range Rover, Rolls Royce"
result = str.split(",")
print("String'i Virgüle Göre Bölünmüş Hali:", result)



# Sayılardan oluşan bir liste
sayilar = [4, 2, 9, 1, 5, 6]

# Listedeki maksimum elemanı bulma
max_sayi = max(sayilar)
print("Maksimum Sayı:", max_sayi)

# Listedeki minimum elemanı bulma
min_sayi = min(sayilar)
print("Minimum Sayı:", min_sayi)

# Stringlerden oluşan bir liste
meyveler = ["muz", "çilek", "karpuz"]

# Alfabetik olarak en büyük ve en küçük elemanı bulma
max_meyve = max(meyveler)
min_meyve = min(meyveler)
print("Alfabetik Olarak Maksimum Meyve:", max_meyve)
print("Alfabetik Olarak Minimum Meyve:", min_meyve)



# Liste Elemanlarına Erişim
# Listeler sıralı olduğundan, her bir elemana indeks ile erişebiliriz. İndeksler 0'dan başlar.
ilk_eleman = liste1[0]  # İlk eleman
son_eleman = liste2[-1]  # Son eleman

print("Liste1'in İlk Elemanı:", ilk_eleman)
print("Liste2'nin Son Elemanı:", son_eleman)



# Listelerde Dilimleme (Slicing)
alt_liste = liste1[1:4]  # 1. indeksten 4. indekse kadar (4. indeks dahil değil)
print("Liste1'in Dilimlenmiş Hali:", alt_liste)



# Listelerde Eleman Değiştirme- Liste Elemanlarını Güncelleme
liste1[0] = 10  # İlk elemanı 10 ile değiştirme
print("Liste1'in Güncellenmiş Hali:", liste1)



# Listelere Eleman Ekleme
# append() metodu: Listenin sonuna eleman ekler
liste1.append(6)
print("Liste1'e Eleman Eklenmiş Hali:", liste1)


# insert() metodu: Belirtilen indekse eleman ekler
liste1.insert(1, 15)
print("Liste1'e Belirtilen İndekste Eleman Eklenmiş Hali:", liste1)

# extend() metodu: Başka bir listeyi mevcut listenin sonuna ekler
liste1.extend([7, 8, 9])
print("Liste1'e Başka Bir Liste Eklenmiş Hali:", liste1)



# Listelerden Eleman Silme
# remove() metodu: Belirtilen değeri listeden siler
liste1.remove(10)
print("Liste1'den Eleman Silinmiş Hali:", liste1)

# pop() metodu: Belirtilen indeksteki elemanı siler ve döner. Eğer indeks belirtilmezse son elemanı siler ve döner.
silinen_eleman = liste1.pop(0)
print("Liste1'den İlk Eleman Silinmiş Hali:", liste1)
print("Silinen Eleman:", silinen_eleman)

# del ifadesi: Belirtilen indeksteki elemanı siler
del liste1[1]
print("Liste1'den Belirtilen İndeksteki Eleman Silinmiş Hali:", liste1)

# clear() metodu: Listedeki tüm elemanları siler
liste1.clear()
print("Liste1'in Tüm Elemanları Silinmiş Hali:", liste1)



# Listelerde Sıralama
sayilar = [4, 2, 9, 1, 5, 6]
sayilar.sort()  # Küçükten büyüğe sıralar
print("Sıralanmış Sayılar:", sayilar)

sayilar.sort(reverse=True)  # Büyükten küçüğe sıralar
print("Tersten Sıralanmış Sayılar:", sayilar)

# String Listesini Sıralama
meyveler = ["elma", "armut", "kiraz"]
meyveler.sort()
print("Sıralanmış Meyveler:", meyveler)



# Listeleri Ters Çevirme (reverse)
sayilar.reverse()
print("Ters Çevrilmiş Sayılar:", sayilar)



# Listeyi Sıralama ve Yeni Bir Listeye Döndürme (sorted)
sorted_liste = sorted(liste2)
print("Sıralanmış Liste2:", sorted_liste)



# Listelerde Eleman Sayısını Sayma (count)
meyve_sayisi = meyveler.count("ananas")
print("Ananas Sayısı:", meyve_sayisi)



# Bir Elemanın İlk İndeksini Bulma (index)
ananas_indeksi = meyveler.index("ananas")
print("Ananas'nın İlk İndeksi:", ananas_indeksi)



# Listelerde Kopyalama
# copy() metodu: Listeyi kopyalar
liste_kopyasi = liste2.copy()
print("Kopyalanmış Liste:", liste_kopyasi)



# Listelerin Birleştirilmesi
birlesik_liste = liste2 + meyveler
print("Birleştirilmiş Liste:", birlesik_liste)



# Liste Uzunluğu
liste_uzunlugu = len(liste2)
print("Liste2'nin Uzunluğu:", liste_uzunlugu)



# Listeyi Tekrarlama-Çoğaltma (Repetition)
tekrar_liste = liste2 * 3
print("Tekrarlanmış Liste:", tekrar_liste)


# Nested Lists (İç İçe Listeler)
nested_list = [1, 2, [3, 4], 5]
print("İç İçe Liste:", nested_list)
print("İç İçe Liste'nin 3. Elemanı:", nested_list[2])
print("İç İçe Liste'nin 3. Elemanının 2. Elemanı:", nested_list[2][1])



# Liste ile Değişken Atama (Unpacking)
meyve_listesi = ["ananas", "mango", "kivi"]
meyve1, meyve2, meyve3 = meyve_listesi
print("Meyve 1:", meyve1)
print("Meyve 2:", meyve2)
print("Meyve 3:", meyve3)



# Liste ile Değişkenlerin Değerlerini Değiştirme
a = 5
b = 10
print("a ve b'nin Değerleri (Önce):", a, b)
a, b = b, a
print("a ve b'nin Değerleri (Sonra):", a, b)

# List Comprehension
# List comprehension, kısa ve öz bir şekilde liste oluşturmayı sağlar.
# Örnek: 0'dan 9'a kadar olan sayıların karesini içeren bir liste oluşturma
kareler = [x**2 for x in range(10)]
print("Kareler Listesi:", kareler)
