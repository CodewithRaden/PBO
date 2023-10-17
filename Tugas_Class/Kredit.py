class Kredit_Mobil:
    def choice(self):
        stop = input("Apakah Anda Ingin Mengajukan Kredit : ")
        if stop.lower() == "ya":
            print('\n===============================')
            print("Tipe Pengajuan Kredit : ")
            print("1. Pengajuan Kredit Perorangan")
            print("2. Pengajuan Kredit Perusahaan")
            print('===============================')
            pilihan = int(input("Masukan Pilihan Anda : "))

            if pilihan == 1:
                print(
                    """
        Syarat pengajuan kredit perorangan adalah:
        ◼ KTP Suami + Istri
        ◼ Kartu Keluarga
        ◼ NPWP
        ◼ PBB / AJB Rumah
        ◼ Rekening tabungan 3 bln terakhir
        ◼ Slip gaji bila bekerja, SKU bila \n""")
                
                satu_input = input("Apakah Semua Syarat Diatas Terpenuhi : ")
                if satu_input.lower() == "ya" or satu_input.lower() == "iya" or satu_input.lower() == "y":
                    print("Pengajuan Kredit Anda Diterima")
                else:
                    print("Pengajuan Kredit Anda Ditolak")
            elif pilihan == 2:
                print(
                    """
        Syarat pengajuan kredit perusahaan adalah:
        ◼ Fotocopy akte pendirian & perubahannya
        ◼ Fotocopy pengesahan kehakiman
        ◼ Fotocopy SIUP, NPWP, SITU / Domisili, TDP
        ◼ Fotocopy Rek. Koran 3 bulan terakhir
        ◼ Fotocopy KTP direksi & komisaris\n""")
                
                dua_input = input("Apakah Semua Syarat Diatas Terpenuhi : ")
                if dua_input.lower() == "ya" or dua_input.lower() == 'iya' or dua_input.lower() == 'y':
                    print("Pengajuan Kredit Anda Diterima")
                else:
                    print("Pengajuan Kredit Anda Ditolak")
            else:
                print("Invalid")
        else:
            print("Program Selesai")
