# Python'da Listeler: Temel Veri Türleri ve İşlemler

# Liste Nedir?
# Liste, Python'da birden fazla öğeyi bir arada saklamak için kullanılan bir veri yapısıdır. 
# Listeler, sıralı ve değiştirilebilir (mutable) veri tipleridir. Farklı veri tiplerini bir arada barındırabilirler.

# Python'da Liste Tanımlama
liste1 = [1, 2, 3, 4, 5]  # Tam sayılardan oluşan bir liste
liste2 = ["ananas", "mango", "kivi"]  # Metinlerden (string) oluşan bir liste
liste3 = [1, "ananas", 3.5, True]  # Farklı veri tiplerinden oluşan bir liste
liste4 = []  # Boş bir liste

print("Liste 1:", liste1)
print("Liste 2:", liste2)
print("Liste 3:", liste3)
print("Boş Liste:", liste4)



# Liste Elemanlarına Erişim
# Listeler sıralı olduğundan, her bir elemana indeks ile erişebiliriz. İndeksler 0'dan başlar.

ilk_eleman = liste1[0]  # İlk eleman
son_eleman = liste2[-1]  # Son eleman

print("Liste1'in İlk Elemanı:", ilk_eleman)
print("Liste2'nin Son Elemanı:", son_eleman)



# Listelerde Dilimleme (Slicing)
alt_liste = liste1[1:4]  # 1. indeksten 4. indekse kadar (4. indeks dahil değil)
print("Liste1'in Dilimlenmiş Hali:", alt_liste)



# Listelerde Eleman Değiştirme
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



# Listeleri Ters Çevirme
sayilar.reverse()
print("Ters Çevrilmiş Sayılar:", sayilar)



# Listelerde Eleman Sayısını Sayma (count)
meyve_sayisi = meyveler.count("elma")
print("Elma Sayısı:", meyve_sayisi)



# Bir Elemanın İlk İndeksini Bulma (index)
elma_indeksi = meyveler.index("elma")
print("Elma'nın İlk İndeksi:", elma_indeksi)



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



# Listeyi Tekrarlama (Repetition)
tekrar_liste = liste2 * 3
print("Tekrarlanmış Liste:", tekrar_liste)