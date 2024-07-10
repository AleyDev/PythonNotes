# Python'da Fonksiyonlar ve Değişkenlerin Kapsamı



# 1. Global Değişkenler
# Global değişkenler, tüm fonksiyonların dışında tanımlanan ve programın herhangi bir yerinden erişilebilen değişkenlerdir.
global_degisken = "Bu bir global değişkendir."

def global_fonksiyon():
    """
    Bu fonksiyon global bir değişkeni kullanır.
    """
    # Global değişkene erişim
    print(global_degisken)

global_fonksiyon()




# 2. Yerel (Local) Değişkenler
# Yerel değişkenler, bir fonksiyonun içinde tanımlanan ve sadece o fonksiyon içinde erişilebilen değişkenlerdir.
def yerel_fonksiyon():
    """
    Bu fonksiyon yerel bir değişken tanımlar.
    """
    yerel_degisken = "Bu bir yerel değişkendir."
    print(yerel_degisken)

yerel_fonksiyon()

# Yerel değişken fonksiyon dışında erişilemez
# Aşağıdaki satır hata verecektir
# print(yerel_degisken)




# 3. Global Değişkeni Fonksiyon İçinde Değiştirme
# Bir global değişkeni fonksiyon içinde değiştirmek için 'global' anahtar kelimesi kullanılır.
sayac = 0

def sayaci_artir():
    """
    Bu fonksiyon global değişkeni artırır.
    """
    global sayac
    sayac += 1
    print(f"Sayac: {sayac}")

sayaci_artir()
sayaci_artir()




# 4. Global ve Yerel Değişkenlerin Etkileşimi
# Aynı isimli bir global ve yerel değişken olabilir. Bu durumda, fonksiyon içinde yerel değişken kullanılır.
x = "global x"

def yerel_ve_global():
    """
    Bu fonksiyon aynı isimde bir global ve yerel değişken tanımlar.
    """
    x = "yerel x"
    print(f"Fonksiyon içindeki x: {x}")

yerel_ve_global()
print(f"Fonksiyon dışındaki x: {x}")




# 5. İç İçe Fonksiyonlar ve Kapsam
# İç içe fonksiyonlarda, iç fonksiyon dış fonksiyonun yerel değişkenlerine erişebilir.
def dis_fonksiyon():
    """
    Bu fonksiyon içinde başka bir fonksiyon tanımlar.
    """
    y = "dis fonksiyon y"

    def ic_fonksiyon():
        """
        Bu iç fonksiyon dış fonksiyonun yerel değişkenine erişir.
        """
        print(f"İç fonksiyon içindeki y: {y}")

    ic_fonksiyon()

dis_fonksiyon()




# 6. Nonlocal Anahtar Kelimesi
# 'nonlocal' anahtar kelimesi, iç içe fonksiyonlarda dış fonksiyonun yerel değişkenini değiştirmek için kullanılır.
def dis_fonksiyon2():
    """
    Bu fonksiyon içinde başka bir fonksiyon tanımlar ve nonlocal anahtar kelimesini kullanır.
    """
    z = "dis fonksiyon z"

    def ic_fonksiyon2():
        """
        Bu iç fonksiyon dış fonksiyonun yerel değişkenini değiştirir.
        """
        nonlocal z
        z = "degistirilmis z"
        print(f"İç fonksiyon içindeki z: {z}")

    ic_fonksiyon2()
    print(f"Dış fonksiyon içindeki z: {z}")

dis_fonksiyon2()




# Fonksiyonların temel kullanımları ve değişkenlerin kapsamları bu şekildedir.
# Global değişkenler programın herhangi bir yerinden erişilebilirken, yerel değişkenler sadece tanımlandıkları fonksiyon içinde erişilebilir.
# 'global' ve 'nonlocal' anahtar kelimeleri, değişkenlerin kapsamını kontrol etmek için kullanılır.
