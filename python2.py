

class Kitab:
    def __init__(self, ad, başlıq, yazar, status=False):
        self.ad = ad
        self.başlıq = başlıq
        self.yazar = yazar
        self.status = status

class Kitabxana:
    def __init__(self):
        self.kitablar = []

    def kitab_əlavə_et(self, kitab):
        self.kitablar.append(kitab)

    def var_olan_kitablar(self):
        return [kitab for kitab in self.kitablar if kitab.status==True]

    def kitab_borc_ver(self, başlıq):
        for kitab in self.kitablar:
            if kitab.başlıq == başlıq:
                kitab.status = True
                return f"{kitab.başlıq} başlıqlı kitabı verdiniz."
        return "Bu başlığa uyğun kitab tapılmadı."

    def kitab_geri_qaytar(self, başlıq):
        for kitab in self.kitablar:
            if kitab.başlıq == başlıq:
                kitab.status = False
                return f"{kitab.başlıq} başlıqlı kitab qaytarıldı."
        return "Bu başlığa uyğun kitab tapılmadı."

    def borc_verilmiş_kitablar(self):
        return [kitab for kitab in self.kitablar if not kitab.status]


