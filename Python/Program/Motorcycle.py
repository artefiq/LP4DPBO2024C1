from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plat_nomor="", merk="", tahun_pembuatan="", warna="", tipe_motor="", kapasitas_tangki=""):
        """
        Inisialisasi objek Motorcycle dengan atribut-atributnya.

        Parameters:
        plat_nomor (str): Nomor plat kendaraan.
        merk (str): Merk kendaraan.
        tahun_pembuatan (str): Tahun pembuatan kendaraan.
        warna (str): Warna kendaraan.
        tipe_motor (str): Tipe motor.
        kapasitas_tangki (str): Kapasitas tangki bahan bakar kendaraan.
        """
        super().__init__(plat_nomor, merk, tahun_pembuatan, warna)
        self.__tipe_motor = tipe_motor
        self.__kapasitas_tangki = kapasitas_tangki

    def display_info(self):
        """
        Menampilkan informasi kendaraan seperti plat nomor, merk, tahun pembuatan, warna,
        tipe motor, dan kapasitas tangki.
        """
        super().display_info()
        print(f"Tipe Motor: {self.__tipe_motor}")
        print(f"Kapasitas Tangki: {self.__kapasitas_tangki} liter")

    def getTipeMotor(self):
        """
        Mendapatkan tipe motor.

        Returns:
        str: Tipe motor kendaraan.
        """
        return self.__tipe_motor
    
    def setTipeMotor(self, tipe_motor):
        """
        Mengatur tipe motor.

        Parameters:
        tipe_motor (str): Tipe motor kendaraan.
        """
        self.__tipe_motor = tipe_motor;

    def getKapasitasTangki(self):
        """
        Mendapatkan kapasitas tangki bahan bakar kendaraan.

        Returns:
        str: Kapasitas tangki kendaraan dalam liter.
        """
        return self.__kapasitas_tangki
        
    def setKapasitasTangki(self, kapasitas_tangki):
        """
        Mengatur kapasitas tangki bahan bakar kendaraan.

        Parameters:
        kapasitas_tangki (str): Kapasitas tangki kendaraan dalam liter.
        """
        self.__kapasitas_tangki = kapasitas_tangki;
