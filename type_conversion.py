# Python'da Kapalı (Implicit) Tip Dönüşümü
# Python bazı durumlarda veri tiplerini otomatik olarak dönüştürür
# Bu genellikle daha küçük bir veri tipinin daha büyük bir veri tipine dönüştürülmesiyle olur.

# Örnek: integer (tamsayı) ve float (ondalık sayı) arasındaki kapalı tip dönüşümü
int_num = 10  # integer
float_num = 5.5  # float

# Python, int_num + float_num işlemini gerçekleştirirken int_num'u otomatik olarak float'a dönüştürür
result = int_num + float_num
print("Kapalı Tip Dönüşümü Sonucu:", result)
print("Sonucun Veri Tipi:", type(result))  # Sonucun tipi float olacaktır

# Python'da Açık (Explicit) Tip Dönüşümü
# Veri tiplerini açıkça belirtmek için Python'un yerleşik fonksiyonlarını kullanırız.
# Bu işlemi manuel olarak yaparız.

# Örnek: String'i (metin) integer'a (tamsayı) dönüştürme
str_num = "123"  # string

# int() fonksiyonu string'i integer'a dönüştürür
int_num = int(str_num)
print("Açık Tip Dönüşümü ile String'den Integer'a:", int_num)
print("Dönüştürülen Veri Tipi:", type(int_num))  # Sonucun tipi int olacaktır

# Örnek: Integer'ı (tamsayı) string'e (metin) dönüştürme
int_num = 456  # integer

# str() fonksiyonu integer'ı string'e dönüştürür
str_num = str(int_num)
print("Açık Tip Dönüşümü ile Integer'dan String'e:", str_num)
print("Dönüştürülen Veri Tipi:", type(str_num))  # Sonucun tipi str olacaktır

# Örnek: Float'ı (ondalık sayı) integer'a (tamsayı) dönüştürme
float_num = 7.89  # float

# int() fonksiyonu float'ı integer'a dönüştürür
# Bu işlem ondalık kısmı keser ve sadece tam kısmı alır
int_num = int(float_num)
print("Açık Tip Dönüşümü ile Float'dan Integer'a:", int_num)
print("Dönüştürülen Veri Tipi:", type(int_num))  # Sonucun tipi int olacaktır

# Örnek: List'i (liste) tuple'a (demet) dönüştürme
list_data = [1, 2, 3, 4]  # list

# tuple() fonksiyonu list'i tuple'a dönüştürür
tuple_data = tuple(list_data)
print("Açık Tip Dönüşümü ile List'den Tuple'a:", tuple_data)
print("Dönüştürülen Veri Tipi:", type(tuple_data))  # Sonucun tipi tuple olacaktır

# Örnek: Tuple'ı (demet) list'e (liste) dönüştürme
tuple_data = (5, 6, 7, 8)  # tuple

# list() fonksiyonu tuple'ı list'e dönüştürür
list_data = list(tuple_data)
print("Açık Tip Dönüşümü ile Tuple'dan List'e:", list_data)
print("Dönüştürülen Veri Tipi:", type(list_data))  # Sonucun tipi list olacaktır

# Örnek: Boolean'ı (mantıksal) integer'a (tamsayı) dönüştürme
bool_val = True  # boolean

# int() fonksiyonu boolean'ı integer'a dönüştürür
int_val = int(bool_val)
print("Açık Tip Dönüşümü ile Boolean'dan Integer'a:", int_val)
print("Dönüştürülen Veri Tipi:", type(int_val))  # Sonucun tipi int olacaktır

# Örnek: Integer'ı (tamsayı) boolean'a (mantıksal) dönüştürme
int_num = 0  # integer

# bool() fonksiyonu integer'ı boolean'a dönüştürür
bool_val = bool(int_num)
print("Açık Tip Dönüşümü ile Integer'dan Boolean'a:", bool_val)
print("Dönüştürülen Veri Tipi:", type(bool_val))  # Sonucun tipi bool olacaktır

# Örnek: String'i (metin) float'a (ondalık sayı) dönüştürme
str_num = "3.14"  # string

# float() fonksiyonu string'i float'a dönüştürür
float_num = float(str_num)
print("Açık Tip Dönüşümü ile String'den Float'a:", float_num)
print("Dönüştürülen Veri Tipi:", type(float_num))  # Sonucun tipi float olacaktır

# Örnek: Integer'ı (tamsayı) float'a (ondalık sayı) dönüştürme
int_num = 100  # integer

# float() fonksiyonu integer'ı float'a dönüştürür
float_num = float(int_num)
print("Açık Tip Dönüşümü ile Integer'dan Float'a:", float_num)
print("Dönüştürülen Veri Tipi:", type(float_num))  # Sonucun tipi float olacaktır

# Örnek: Boolean'ı (mantıksal) string'e (metin) dönüştürme
bool_val = False  # boolean

# str() fonksiyonu boolean'ı string'e dönüştürür
str_val = str(bool_val)
print("Açık Tip Dönüşümü ile Boolean'dan String'e:", str_val)
print("Dönüştürülen Veri Tipi:", type(str_val))  # Sonucun tipi str olacaktır

# Örnek: String'i (metin) boolean'a (mantıksal) dönüştürme
str_val = "True"  # string

# bool() fonksiyonu string'i boolean'a dönüştürür
# Not: Python'da boş olmayan her string True olarak değerlendirilir
bool_val = bool(str_val)
print("Açık Tip Dönüşümü ile String'den Boolean'a:", bool_val)
print("Dönüştürülen Veri Tipi:", type(bool_val))  # Sonucun tipi bool olacaktır

# Örnek: Dictionary'yi (sözlük) list'e (liste) dönüştürme (anahtarları kullanarak)
dict_data = {1: 'a', 2: 'b', 3: 'c'}  # dictionary

# list() fonksiyonu dictionary'nin anahtarlarını list'e dönüştürür
list_keys = list(dict_data)
print("Açık Tip Dönüşümü ile Dictionary'den List'e (anahtarlar):", list_keys)
print("Dönüştürülen Veri Tipi:", type(list_keys))  # Sonucun tipi list olacaktır

# Örnek: Set'i (küme) list'e (liste) dönüştürme
set_data = {1, 2, 3, 4}  # set

# list() fonksiyonu set'i list'e dönüştürür
list_data = list(set_data)
print("Açık Tip Dönüşümü ile Set'den List'e:", list_data)
print("Dönüştürülen Veri Tipi:", type(list_data))  # Sonucun tipi list olacaktır
