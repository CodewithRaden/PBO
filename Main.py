class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    def print(self):
        print(self.nama)
        print(self.nim)

m1 = Mahasiswa('Raden',221)
m1.print()