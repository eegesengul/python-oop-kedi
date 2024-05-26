class Kedi:
    def __init__(self, isim, yas, cinsiyet):
        self.isim = isim
        self.yas = yas
        self.cinsiyet = cinsiyet

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}"

    def miyavla(self):
        return f"{self.isim} miyavlıyor!"

    def __str__(self):
        return self.bilgileri_goster()


class ScottishFold(Kedi):
    def __init__(self, isim, yas, cinsiyet, kulak_tipi):
        super().__init__(isim, yas, cinsiyet)
        self.kulak_tipi = kulak_tipi

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}, Kulak Tipi: {self.kulak_tipi}"

    def __str__(self):
        return self.bilgileri_goster()


class BritishShorthair(Kedi):
    def __init__(self, isim, yas, cinsiyet, agirlik):
        super().__init__(isim, yas, cinsiyet)
        self.agirlik = agirlik

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}, Ağırlık: {self.agirlik} kg"

    def __str__(self):
        return self.bilgileri_goster()


class Sphynx(Kedi):
    def __init__(self, isim, yas, cinsiyet, tuy_durumu):
        super().__init__(isim, yas, cinsiyet)
        self.tuy_durumu = tuy_durumu

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}, Tüy Durumu: {self.tuy_durumu}"

    def __str__(self):
        return self.bilgileri_goster()


def kedi_olustur():
    try:
        isim = input("Kedinin ismi: ").strip()
        yas = int(input("Kedinin yaşı: ").strip())
        cinsiyet = input("Kedinin cinsiyeti: ").strip()
        tur = input("Kedinin türü (ScottishFold/BritishShorthair/Sphynx): ").strip().capitalize()

        if tur == "Scottishfold":
            kulak_tipi = input("Kedinin kulak tipi: ").strip()
            return ScottishFold(isim, yas, cinsiyet, kulak_tipi)
        elif tur == "Britishshorthair":
            agirlik = float(input("Kedinin ağırlığı: ").strip())
            return BritishShorthair(isim, yas, cinsiyet, agirlik)
        elif tur == "Sphynx":
            tuy_durumu = input("Kedinin tüy durumu: ").strip()
            return Sphynx(isim, yas, cinsiyet, tuy_durumu)
        else:
            print("Geçersiz tür!")
            return None
    except ValueError as e:
        print(f"Yanlış veri tipi girdiniz: {e}")
        return None


kedi1 = ScottishFold("Lülü", 3, "Dişi", "Katlanmış")
kedi2 = BritishShorthair("Nisan", 2, "Dişi", 4.5)
kedi3 = Sphynx("Fiko", 4, "Erkek", "Tüysüz")

print(kedi1)
print(kedi2)
print(kedi3)

print(kedi1.miyavla())
print(kedi2.miyavla())
print(kedi3.miyavla())

yeni_kedi = kedi_olustur()
if yeni_kedi:
    print(yeni_kedi)
    print(yeni_kedi.miyavla())
