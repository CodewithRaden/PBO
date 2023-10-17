class Car_Tipe:
    def dapatkan_tipe(self, varian):
        tipe_mobil = {
            1: "MPV",
            2: "MPV",
            3: "SUV",
            4: "SUV",
            5: "HATCHBACK",
            6: "HATCHBACK",
            7: "SEDAN",
            8: "SEDAN",
            9: "COMMERCIAL",
            10: "COMMERCIAL",
        }
        return tipe_mobil.get(varian)
    
    def cek_tipe(self):
        input_user = int(input("Masukkan Varian Mobil untuk Di Cek Tipenya: "))
        tipe_mobil = self.dapatkan_tipe(input_user)
        if tipe_mobil:
            print(f"Tipe Mobil: {tipe_mobil}")
        else:
            print("Pilihan Anda Tidak Valid")
        print("\n")
