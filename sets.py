# Python'da Set (Küme): Temel Veri Türleri ve İşlemler

# Set Nedir?
# Set, benzersiz (unique) ve sırasız (unordered) elemanlardan oluşan bir veri yapısıdır.
# Set'ler, indekslenemez, sıralanamaz, güncellenemez,elemanlar tekrarlanamaz. Eleman ekler ya da silebiliriz.
# Set'ler küme işlemleri (birleşim, kesişim, fark, vb.) için kullanışlıdır.
# Set'ler süslü parantez {} kullanılarak tanımlanır.


# Python'da Set Tanımlama
kume1 = {1, 2, 3, 4, 5}  # Tam sayılardan oluşan bir set
print("Küme 1:", kume1)


# Boş bir set tanımlama
bos_kume = set()
print("Boş Küme:", bos_kume)



# Set'e Eleman Ekleme
# add() metodu: Set'e bir eleman ekler
kume1.add(6)
print("Eleman Eklenmiş Küme 1:", kume1)



# Set'ten Eleman Silme
# remove() metodu: Belirtilen elemanı set'ten siler. Eleman yoksa hata verir.
kume1.remove(6)
print("Eleman Silinmiş Küme 1:", kume1)

# discard() metodu: Belirtilen elemanı set'ten siler. Eleman yoksa hata vermez.
kume1.discard(5)
print("Eleman Silinmiş Küme 1 (discard ile):", kume1)

# pop() metodu: Set'ten rastgele bir eleman siler ve döner
rastgele_eleman = kume1.pop()
print("Rastgele Silinen Eleman:", rastgele_eleman)
print("Pop İşleminden Sonra Küme 1:", kume1)

# clear() metodu: Set'teki tüm elemanları siler
kume1.clear()
print("Tüm Elemanları Silinmiş Küme 1:", kume1)



# Set Uzunluğu (Eleman Sayısı)
kume2 = {1, 2, 3}
kume_uzunluk = len(kume2)
print("Küme 2'nin Uzunluğu:", kume_uzunluk)



# Küme İşlemleri
# Birleşim (Union): İki set'in tüm elemanlarını içerir
kume3 = {3, 4, 5}
birlesim = kume2.union(kume3)
print("Birleşim:", birlesim)

# Kesişim (Intersection): İki set'in ortak elemanlarını içerir
kesisim = kume2.intersection(kume3)
print("Kesişim:", kesisim)

# Fark (Difference): İlk set'te olup, ikinci set'te olmayan elemanları içerir
fark = kume2.difference(kume3)
print("Fark:", fark)

# Symmetric Difference (Sembolik Fark): İki set'te de bulunmayan elemanları içerir
sembolik_fark = kume2.symmetric_difference(kume3)
print("Sembolik Fark:", sembolik_fark)

# Alt Küme (Subset) ve Üst Küme (Superset) Kontrolü
kume4 = {1, 2}
print("Küme 4, Küme 2'nin alt kümesi mi?:", kume4.issubset(kume2))
print("Küme 2, Küme 4'ün üst kümesi mi?:", kume2.issuperset(kume4))



# Set Kopyalama
# copy() metodu: Set'i kopyalar
kopya_kume = kume2.copy()
print("Kopyalanmış Küme 2:", kopya_kume)



# Set'lerin Avantajları:
# 1. Hızlı üyelik testi (eleman içerip içermediğini kontrol etme).
# 2. Benzersiz elemanlar içerdiği için tekrar eden elemanları otomatik olarak filtreler.
# 3. Küme teorisi işlemleri (birleşim, kesişim, fark, vb.) için kullanışlıdır.



# Set Kullanım Örnekleri:
# 1. Tekrarlanan elemanların filtrelenmesi
listeden_kume = set([1, 2, 2, 3, 4, 4, 5])
print("Tekrarlanan Elemanların Filtrelenmiş Hali:", listeden_kume)



# 2. İki veri kümesinin karşılaştırılması
ogrenciler1 = {"Aley", "TU", "Ali"}
ogrenciler2 = {"TU", "Enes", "Emirhan"}
ortak_ogrenciler = ogrenciler1.intersection(ogrenciler2)
print("Ortak Öğrenciler:", ortak_ogrenciler)
