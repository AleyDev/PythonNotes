# Python'da Tuples: Temel Veri Türleri ve İşlemler

# Tuple Nedir?
# Tuple, birden fazla öğeyi bir arada saklamak için kullanılan bir veri yapısıdır.
# Tuples, sıralı ve değiştirilemez (immutable) veri tipleridir. Farklı veri tiplerini bir arada barındırabilirler.
# Tuple'lar, parantez () kullanılarak tanımlanır.



# Python'da Tuple Tanımlama
tuple1 = (1, 2, 3, 4, 5)  # Tam sayılardan oluşan bir tuple
tuple2 = ("ananas", "mango", "kivi")  # Metinlerden (string) oluşan bir tuple
tuple3 = (1, "ananas", 3.5, True)  # Farklı veri tiplerinden oluşan bir tuple
tuple4 = ()  # Boş bir tuple

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)
print("Boş Tuple:", tuple4)



# Tek elemanlı bir tuple tanımlama
tek_elemanli_tuple = (5,)  # Tek elemanlı bir tuple (virgül kullanımı gerekli)
print("Tek Elemanlı Tuple:", tek_elemanli_tuple)



# Tuple Elemanlarına Erişim
# Tuple'lar sıralı olduğundan, her bir elemana indeks ile erişebiliriz. İndeksler 0'dan başlar.

ilk_eleman = tuple1[0]  # İlk eleman
son_eleman = tuple2[-1]  # Son eleman

print("Tuple1'in İlk Elemanı:", ilk_eleman)
print("Tuple2'nin Son Elemanı:", son_eleman)



# Tuple'larda Dilimleme (Slicing)
alt_tuple = tuple1[1:4]  # 1. indeksten 4. indekse kadar (4. indeks dahil değil)
print("Tuple1'in Dilimlenmiş Hali:", alt_tuple)



# Tuple'lar Değiştirilemez (Immutable)
# Tuple'lar immutable olduğu için elemanlarını değiştiremeyiz.
# Aşağıdaki satır hata verecektir:
# tuple1[0] = 10
tuple5 = (10,) + tuple1[1:]
print("Yeni Tuple:", tuple5)


# Ancak, tuple'lar yeniden tanımlanabilir:
tuple1 = (10, 2, 3, 4, 5)
print("Yeniden Tanımlanmış Tuple1:", tuple1)



# Tuple'ları Birleştirme (Concatenation)
tuple5 = tuple1 + tuple2
print("Birleştirilmiş Tuple:", tuple5)



# Tuple'ları Çoğaltma (Repetition)
tuple6 = tuple2 * 3
print("Çoğaltılmış Tuple:", tuple6)



# Tuple Eleman Sayısı (Length)
tuple_uzunlugu = len(tuple2)
print("Tuple2'nin Uzunluğu:", tuple_uzunlugu)



# Tuple'da Eleman Sayısını Sayma (count)
meyve_sayisi = tuple2.count("ananas")
print("Ananas Sayısı:", meyve_sayisi)



# Bir Elemanın İlk İndeksini Bulma (index)
# Eğer "elma" tuple içinde yoksa, bu komut hata verecektir. Bu yüzden öncelikle arama yapabiliriz.
if "elma" in tuple2:
    elma_indeksi = tuple2.index("elma")
    print("Elma'nın İlk İndeksi:", elma_indeksi)
else:
    print("Elma tuple2 içinde bulunamadı.")


# Var Olan Elemanı Arama
mango_indeksi = tuple2.index("mango")
print("Mango'nun İlk İndeksi: ", mango_indeksi)



# Tuple İçinde Arama
arama_sonucu = "ananas" in tuple2
print("Ananas tuple2 içinde mi?:", arama_sonucu)



# Tuple'dan Listeye Dönüştürme
tuple_to_list = list(tuple1)
print("Tuple'dan Listeye Dönüştürülmüş Hali:", tuple_to_list)



# Listeyi Tuple'a Dönüştürme
list_to_tuple = tuple(tuple_to_list)
print("Listeden Tuple'a Dönüştürülmüş Hali:", list_to_tuple)



# Nested Tuples (İç İçe Tuple'lar)
nested_tuple = (1, 2, (3, 4), 5)
print("İç İçe Tuple:", nested_tuple)
print("İç İçe Tuple'ın 3. Elemanı:", nested_tuple[2])
print("İç İçe Tuple'ın 3. Elemanının 2. Elemanı:", nested_tuple[2][1])



# Tuple ile Değişken Atama (Unpacking)
meyve_tuple = ("ananas", "mango", "kivi")
meyve1, meyve2, meyve3 = meyve_tuple
print("Meyve 1:", meyve1)
print("Meyve 2:", meyve2)
print("Meyve 3:", meyve3)



# Tuple ile Değişkenlerin Değerlerini Değiştirme
a = 5
b = 10
print("a ve b'nin Değerleri (Önce):", a, b)
a, b = b, a
print("a ve b'nin Değerleri (Sonra):", a, b)



# Tuple'ların Avantajları:
# 1. Değiştirilemez oldukları için veri güvenliği sağlar.
# 2. Daha az bellek kullanırlar.
# 3. Tuple'lar dictionary'de anahtar olarak kullanılabilirler.

# Tuple Kullanım Alanları
# 1. Verilerin Sabit Kalması Gerektiği Durumlar:
# Tuple'lar, veri değiştirilemez olduğundan, verilerin sabit kalması gereken durumlarda kullanılır.
# Örneğin, sabit konfigürasyon ayarları veya koordinat değerleri gibi.

# 2. Dictionary Anahtarları Olarak Kullanım:
# Tuple'lar immutable olduğu için dictionary anahtarı olarak kullanılabilirler.
koordinatlar = {(40.7128, 74.0060): "New York", (34.0522, 118.2437): "Los Angeles"}
print("Koordinatlar:", koordinatlar)


# 3. Farklı Veri Setlerini Bir Araya Getirmek:
# Tuple'lar, farklı veri setlerini bir arada tutmak için kullanılabilir.
ogrenci_bilgileri = ("Aley", "Ky", 24, "Yazılım Geliştirici")
print("Öğrenci Bilgileri:", ogrenci_bilgileri)
