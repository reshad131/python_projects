

class Bank:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def depozit(self, mebleg):
        self.balans += mebleg

    def cixar(self, mebleg):
        if mebleg <= self.balans:
            self.balans -= mebleg
        else:
            print("Kifayet qeder vesait yoxdur")

    def balansi_goster(self):
        print(f"Hesab Nomresi: {self.hesab_nomresi}, Balans: {self.balans}")



class KreditHesabi(Bank):
    def __init__(self, hesab_nomresi, balans, kredit_meblegi):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meblegi = kredit_meblegi

    def kredit_ver(self):
        self.balans += self.kredit_meblegi

    def kredit_al(self):
        if self.kredit_meblegi <= self.balans:
            self.balans -= self.kredit_meblegi
            self.kredit_meblegi = 0
        else:
            print("Kredit borcunu odemek ücün kifayet qeder vesait yoxdur")

    def ayliq_odenis_hesabla(self):
        if self.kredit_meblegi > 0:
            ayliq_odenis = self.kredit_meblegi / 12
            ayliq_odenis = round(ayliq_odenis, 2)
            print(f"Ayliq odenis {ayliq_odenis}")
        else:
            print("Odenis yoxdur ")

# Bank_hesabi = Bank("1234567" , 1000)
# Bank_hesabi.depozit(1000)
# Bank_hesabi.balansi_goster()
kredit_hesabi = KreditHesabi("786876786" , 50088 , 10000)
# kredit_hesabi.kredit_ver(5000)
kredit_hesabi.balansi_goster()
# kredit_hesabi.kredit_al()
# kredit_hesabi.balansi_goster()
kredit_hesabi.ayliq_odenis_hesabla()