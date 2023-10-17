from Browsur_Toyota import Browsur_Mobil
from Kredit import Kredit_Mobil
from Mobil_tipe import Car_Tipe

def main():
    print("=========================================")
    print("\tHarga Kendaraan Toyota")
    print("=========================================")
    # MPV
    AllNewAvanza = Browsur_Mobil("Varian(1) :  All New Veloz")
    AllNewAvanza.addVar("1.3 MT", "                 233.100.000")
    AllNewAvanza.addVar("1.3 CVT", "                247.800.000")
    AllNewAvanza.tampil()

    AllNewCayla = Browsur_Mobil("Varian(2)  :  All New Cayla")
    AllNewCayla.addVar("1.2 E MT STD", "           160.900.000")
    AllNewCayla.addVar("1.3 E MT", "               163.800.000")
    AllNewCayla.tampil()

    # SUV
    NewRush = Browsur_Mobil("Varian(3)  :  All New Rush")
    NewRush.addVar("1.2 E MT STD", "           278.800.000")
    NewRush.addVar("1.3 E MT", "               163.800.000")
    NewRush.tampil()

    AllNewRaize = Browsur_Mobil("Varian(4)  :  All New Raize")
    AllNewRaize.addVar("1.2 G MT", "               232.400.000")
    AllNewRaize.addVar("1.3 E MT", "               163.800.000")
    AllNewRaize.tampil()

    # HATCHBACK
    NewAgya = Browsur_Mobil("Varian(5)  :  All New Agya")
    NewAgya.addVar("1.2 G MT STD", "          159.700.000")
    NewAgya.addVar("1.2 G AT STD", "          173.300.000")
    NewAgya.tampil()

    NewYaris = Browsur_Mobil("Varian(6)  :  All New Yaris")
    NewYaris.addVar("1.2 G CTV 3 AV", "        295.800.000")
    NewYaris.addVar("1.5 G S MT GR 3 AB", "    308.100.000")
    NewYaris.tampil()

    # SEDAN
    AllNewCorrola = Browsur_Mobil("Varian(7)  :  All New Corrola Altis")
    AllNewCorrola.addVar("1.8 HYBRID AT", "         550.900.000")
    AllNewCorrola.tampil()

    AllNewCamry = Browsur_Mobil("Varian(8)  :  All New Camry")
    AllNewCamry.addVar("2.5 V AT", "              741.700.000")
    AllNewCamry.addVar("1.5 L AT", "              874.600.000")
    AllNewCamry.tampil()

    # CORMECIAL
    AllNewHiace = Browsur_Mobil("Varian(9)  :  All New Hiace")
    AllNewHiace.addVar("COMUTTER MT", "           545.000.000")
    AllNewHiace.addVar("PREMIO MT", "             630.000.000")
    AllNewHiace.tampil()

    AllNewHilux = Browsur_Mobil("Varian(10)  :  All New Hilux")
    AllNewHilux.addVar("SC 2.0 MT BSN", "         269.900.000")
    AllNewHilux.addVar("SC 2.4 MT DSL", "         290.900.000")
    AllNewHilux.tampil()

    #CEK TIPE MOBIL
    Checker = Car_Tipe()
    Checker.cek_tipe()

    #KREDIT CEK
    eligible = Kredit_Mobil()
    eligible.choice()


main()
