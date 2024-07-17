# Python'da Nesne Yönelimli Programlama (OOP)

# OOP, programları nesneler kullanarak modellemeyi sağlayan bir programlama paradigmasıdır.
# Nesneler, veriler (özellikler) ve bu veriler üzerinde işlem yapan fonksiyonlar (metotlar) içerir.



# 1. Sınıf Tanımlama
# Bir sınıf, nesnelerin şablonudur. Sınıflar, nesnelerin özelliklerini ve davranışlarını tanımlar.
class Araba:
    """
    Bu sınıf bir araba modelini temsil eder.
    """

    # Sınıfın başlatıcı metodu (__init__) nesne oluşturulduğunda çağrılır.
    def __init__(self, marka, model, yil):
        self.marka = marka  # Arabanın markası
        self.model = model  # Arabanın modeli
        self.yil = yil      # Arabanın üretim yılı

    # Sınıfın metotları
    def bilgi_goster(self):
        """
        Arabanın bilgilerini ekrana yazdırır.
        """
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}")

    def calistir(self):
        """
        Arabayı çalıştırır.
        """
        print(f"{self.marka} {self.model} çalıştırılıyor...")




# 2. Nesne Oluşturma
# Sınıf tanımlandıktan sonra nesneler oluşturulabilir.
araba1 = Araba("Range Rover", "Sports", 2024)
araba2 = Araba("Audi", "RS7", 2024)




# 3. Nesne Metotlarını Kullanma
# Nesneler oluşturulduktan sonra, bu nesnelerin metotları kullanılabilir.
araba1.bilgi_goster()
araba2.bilgi_goster()

araba1.calistir()
araba2.calistir()




# 4. Kalıtım (Inheritance)
# Bir sınıf, başka bir sınıfın özelliklerini ve metotlarını miras alabilir.
class ElektrikliAraba(Araba):
    """
    Bu sınıf, elektrikli arabaları temsil eder ve Araba sınıfından miras alır.
    """
    
    def __init__(self, marka, model, yil, batarya_kapasitesi):
        # Üst sınıfın __init__ metodunu çağırır
        super().__init__(marka, model, yil)
        self.batarya_kapasitesi = batarya_kapasitesi  # Batarya kapasitesi (kWh)

    def bilgi_goster(self):
        """
        Elektrikli arabanın bilgilerini ekrana yazdırır.
        """
        super().bilgi_goster()
        print(f"Batarya Kapasitesi: {self.batarya_kapasitesi} kWh")

    def sarj_et(self):
        """
        Elektrikli arabayı şarj eder.
        """
        print(f"{self.marka} {self.model} şarj ediliyor...")

# Elektrikli araba nesnesi oluşturma
elektrikli_araba = ElektrikliAraba("Tesla", "Model 3", 2021, 75)
elektrikli_araba.bilgi_goster()
elektrikli_araba.sarj_et()




# 5. Polimorfizm (Polymorphism)
# Farklı sınıfların, aynı isimdeki metotları farklı şekilde uygulaması anlamına gelir.
class Bisiklet:
    """
    Bu sınıf bir bisiklet modelini temsil eder.
    """
    
    def __init__(self, marka, vites_sayisi):
        self.marka = marka
        self.vites_sayisi = vites_sayisi

    def bilgi_goster(self):
        """
        Bisikletin bilgilerini ekrana yazdırır.
        """
        print(f"Marka: {self.marka}, Vites Sayısı: {self.vites_sayisi}")


# Nesne oluşturma ve polimorfizm örneği
araclar = [araba1, elektrikli_araba, Bisiklet("Bianchi", 21)]

for arac in araclar:
    arac.bilgi_goster()
