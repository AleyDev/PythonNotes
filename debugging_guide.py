# Python'da Debugging (Hata Ayıklama)

# Debugging, kodunuzdaki hataları bulmak ve düzeltmek için kullanılan bir yöntemdir. 



# 1. Print İfadeleri ile Debugging
# En temel debugging yöntemlerinden biri, kodunuzda çeşitli noktalara print() ifadeleri ekleyerek değişkenlerin değerlerini ve programın akışını izlemektir.
def toplama(a, b):
    # Değişkenlerin değerlerini kontrol et
    print(f"Toplama fonksiyonu çağrıldı: a={a}, b={b}")
    return a + b

# Print ifadeleri ile debugging örneği
sonuc = toplama(3, 5)
print(f"Sonuç: {sonuc}")



# 2. Python Debugger (pdb) Kullanımı
# Python, pdb modülü ile dahili bir hata ayıklama aracı sağlar. pdb kullanarak programınızı adım adım çalıştırabilir, değişkenlerin değerlerini kontrol edebilir ve hataların kaynağını bulunabilir.
import pdb

def bolme(a, b):
    # Debugging başlangıcı
    pdb.set_trace()
    return a / b

# pdb modülü ile debugging örneği
try:
    sonuc = bolme(10, 2)
    print(f"Sonuç: {sonuc}")
except ZeroDivisionError as e:
    print(f"Hata: {e}")



# 3. IDE ve Code Editor Debuggerları
# Birçok modern IDE ve kod editörü, dahili hata ayıklama araçları sunar. Örneğin, Visual Studio Code (VSCode), PyCharm ve diğerleri, breakpoint (kesme noktası) ekleyerek ve adım adım çalıştırarak hata ayıklama imkanı sağlar.


def carpma(a, b):
    return a * b

# IDE debug oturumunda adım adım inceleme yapılabilir.
sonuc = carpma(4, 6)
print(f"Sonuç: {sonuc}")


