# Hata Türleri ve Hata Yönetimi

# Bu bölümde bazı yaygın hata türlerini ve bu hataları nasıl yöneteceğimizi öğreneceğiz.

# Hata Türleri (Exceptions):

# NameError: Tanımlanmamış bir değişken veya fonksiyon adı kullanıldığında oluşur. -> İsimlendirme Hatası
# Örnek: print(a)  # a değişkeni tanımlanmadığı için NameError oluşur.

# ValueError: Geçersiz bir değer verildiğinde oluşur. -> Değişken Hatası
# Örnek: int('1a2')  # '1a2' ifadesi tam sayı olarak dönüştürülemediği için ValueError oluşur.

# ZeroDivisionError: Bir sayının sıfıra bölünmeye çalışılması durumunda oluşur. -> Sıfıra Bölünemez Hatası
# Örnek: print(10/0)  # 10'un sıfıra bölünmesi ZeroDivisionError oluşturur.

# SyntaxError: Kodun yazımında bir hata olduğunda oluşur. -> Yazım Yanlışı Hatası
# Örnek: print('denem'e)  # Tırnak hatası SyntaxError oluşturur.


# Hata Yönetimi (Error Handling):

# Hata yönetimi, kodumuzda oluşabilecek hataları yakalayıp, bu hatalara uygun yanıtlar verebilmemizi sağlar.
# Bunun için try-except bloklarını kullanırız.

# Örnek:
try:
    # Kullanıcıdan iki sayı girmesini isteriz.
    x = int(input('x: '))
    y = int(input('y: '))
    # İlk sayıyı ikinci sayıya böleriz ve sonucu yazdırırız.
    print(x / y)
except ZeroDivisionError:
    # Eğer ikinci sayı 0 ise, bu hata yakalanır ve kullanıcıya bilgi verilir.
    print('Hata: Bir sayı sıfıra bölünemez.')
except ValueError:
    # Eğer kullanıcı sayısal olmayan bir değer girerse, bu hata yakalanır ve kullanıcıya bilgi verilir.
    print('Hata: Lütfen geçerli bir sayı girin.')

# Genel Hata Yakalama:
# Eğer spesifik hataları yakalamak istemiyorsanız, genel anlamda tüm hataları yakalayabilirsiniz.
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x / y)
except:
    print('Hata: Bir şeyler yanlış gitti.')

# else Bloğu Kullanımı:
# Hata oluşmadığında çalışacak bir blok eklemek için else kullanabiliriz.
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x / y)
except:
    print('Hata: Bir şeyler yanlış gitti.')
else:
    # Hata oluşmadığında bu blok çalışır.
    print('Her şey yolunda.')

# Döngü İçinde Hata Yönetimi:
# Hataları sürekli kontrol etmek için while döngüsü ile hata yönetimi yapabiliriz.
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x / y)
    except:
        # Hata aldıkça döngü devam eder ve kullanıcıdan tekrar giriş istenir.
        print('Hata: Bir şeyler yanlış gitti.')
    else:
        # Hata olmadığında döngüden çıkılır.
        break

# finally Bloğu:
# finally bloğu, hata oluşsa da oluşmasa da her zaman çalışır.
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x / y)
    except Exception as ex:
        print('Hata: Bir şeyler yanlış gitti.', ex)  # Hatanın nedenini de yazar.
    else:
        break  # Hata olmadığında döngüden çıkılır.
    finally:
        print('try-except bloğu sonlandı')  # Her durumda çalışacak blok.

# Bu örnekler, kodumuzda oluşabilecek hataları nasıl yöneteceğimizi ve kullanıcıya anlamlı mesajlar nasıl gösterebileceğimizi öğrenmemize yardımcı olacaktır.
