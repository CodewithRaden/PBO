class Browsur_Mobil:
    def __init__(self, nama_mobil):
        self.nama = nama_mobil
        self.model = {}

    def addVar(self, varian, harga):
        self.model[varian] = [harga]

    def tampil(self):
        print(f"{self.nama}")
        for model, [harga] in self.model.items():
            print(f"{model}       {harga}")
        print("\n")
