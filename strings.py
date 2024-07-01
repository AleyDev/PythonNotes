# Python'da Strings: Temel Veri Türleri ve İşlemler
# String Nedir?
# String, karakterlerin bir dizisidir. Metin verilerini saklamak ve işlemek için kullanılır. 
# Python'da stringler, tek tırnak (' '), çift tırnak (" ") veya üç tırnak (''' ''' veya """ """) kullanılarak tanımlanabilir.


# Python'da String Tanımlama
str1 = 'Merhaba Dünya'  # Tek tırnak kullanarak
str2 = "Python programlama"  # Çift tırnak kullanarak
str3 = '''Çok satırlı
bir string'''  # Üç tırnak kullanarak (çok satırlı string)

print(str1)
print(str2)
print(str3)


# String Birleştirme (Concatenation)
str4 = str1 + " - " + str2
print("Birleştirilmiş String:", str4)


# String Çoğaltma (Repetition)
str5 = "Merhaba! " * 3
print("Çoğaltılmış String:", str5)


# String Uzunluğu (Length)
str_length = len(str1)
print("str1 Uzunluğu:", str_length)


# String İçinde Karakter Erişimi (Indexing)
first_char = str1[0]  # İlk karakter
last_char = str1[-1]  # Son karakter
print("İlk Karakter:", first_char)
print("Son Karakter:", last_char)


# String Dilimleme (Slicing)
substring = str1[0:7]  # 0. indeksten 7. indekse kadar (7. indeks dahil değil)
print("Dilimlenmiş String:", substring)


# String'lerin İmmutability Özelliği
# Stringler immutabledir (değiştirilemez), bu yüzden bir karakteri doğrudan değiştiremeyiz.
# Ancak, yeni bir string oluşturabiliriz.
str6 = "Hello World!"
# str6[0] = 'h'  # Bu hata verir
str6 = 'h' + str6[1:]  # Yeni bir string oluşturma
print("Değiştirilmiş String:", str6)


# String İçinde Arama (Search)
search_result = "Python" in str2
print("Python str2 içinde mi?:", search_result)


# String Metodları
# Büyük harfe çevirme
str_upper = str2.upper()
print("Büyük Harfli String:", str_upper)


# Küçük harfe çevirme
str_lower = str2.lower()
print("Küçük Harfli String:", str_lower)


# Sadece ilk harfi büyük yapma
str_capitalize = str2.capitalize()
print("İlk Harfi Büyük String:", str_capitalize)


# Her kelimenin ilk harfini büyük yapma
str_title = str2.title()
print("Her Kelimenin İlk Harfi Büyük String:", str_title)


# Boşlukları kaldırma
str_trim = "   Python programlama   ".strip()
print("Boşlukları Kaldırılmış String:", str_trim)

metin = "$$$%%%Python%%%$$$"
temizlenmis_metin = metin.strip("$%")
print("Orijinal Metin: '", metin, "'", sep="") # Orijinal Metin: '$$$%%%Python%%%$$$'
print("Birden Fazla Karakteri Kaldırılmış Metin: '", temizlenmis_metin, "'", sep="") # Birden Fazla Karakteri Kaldırılmış Metin: 'Python'



# String'i bölme (Split)
str_message = "Hello There. My name is Aley"
str_split = str_message.split() # Boşluk karakteri ayırıcı olarak kullanılır
print("Bölünmüş String:", str_split)

str_split = str_message.split(".") # Nokta ayırıcı olarak kullanılır 
print("Nokta İşaretinden İtibaren Bölünmüş String: ", str_split)


# String'i birleştirme (Join)
str_join = " ".join(str_split) # Boşluk karakteri ayırıcı olarak kullanılır
print("Birleştirilmiş String:", str_join)

fruits = ["ananas", "mango", "kivi"]
str_join1 = ", ".join(fruits) # Virgül ve boşluk ayırıcı olarak kullanılır
print("Birleştirilmiş Metin 2:",str_join1)


# String'de alt string arama (Find)
metin = "Python Programlama Dili ve Python Kütüphaneleri"
str_find = metin.find("Python") # Python ifadesini arıyoruz
print("İlk 'Python' kelimesinin bulunduğu indeks: ", str_find) # Aranan ifadenin bulunduğu ilk indeksi çıktı olarak verir.: 0
# find() ifadesi aranılan değeri bulamazsa, geriye -1 değeri döndürür.


# Startswith: Bir string'in belirtilen bir karakter dizisi ile başlayıp başlamadığını kontrol eder.
str_startswith = str2.startswith('Py')  # str2'in 'Py' ile başlayıp başlamadığını kontrol eder
print("str2 'Py' ile başlıyor mu?:", str_startswith)


# endsWith: Bir string'in belirtilen bir karakter dizisi ile bitip bitmediğini kontrol eder.
str_endswith = str1.endswith('a')  # str1'in 'a' ile bitip bitmediğini kontrol eder
print("str1 'a' ile bitiyor mu?:", str_endswith)


# replace: Bir string içinde belirtilen bir alt string'i başka bir alt string ile değiştirir.
str_replace = str3.replace('bir', 'bu')  # str3 içindeki 'bir'leri 'bu' olarak değiştirir
print("str3 replace sonrası:", str_replace)


# center: Bir string'i belirtilen genişlikte olacak şekilde ortalar.
str_center = str1.center(30, '-')  # str1'i 30 karakter genişliğinde '-' karakterleriyle ortalar
print("str1 30 karakter genişliğinde ortalanmış hali:", str_center)


# String Formatlama
name = "Aley"
age = 24 
formatted_str = f"Benim adım {name} ve {age} yaşındayım."
print("Formatlanmış String:", formatted_str) # 1

print(f"Benim adım {name} ve {age} yaşındayım.") # 2

print("Benim adım {} ve {} yaşındayım.".format(name,age)) # 3



