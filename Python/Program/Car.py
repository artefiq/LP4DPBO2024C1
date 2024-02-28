from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plat_nomor="", merk="", tahun_pembuatan="", warna="", jml_kursi="", jml_pintu=""):
        """
        Inisialisasi objek Car dengan atribut-atributnya.

        Parameters:
        plat_nomor (str): Nomor plat kendaraan.
        merk (str): Merk kendaraan.
        tahun_pembuatan (str): Tahun pembuatan kendaraan.
        warna (str): Warna kendaraan.
        jml_kursi (str): Jumlah kursi dalam kendaraan.
        jml_pintu (str): Jumlah pintu dalam kendaraan.
        """
        super().__init__(plat_nomor, merk, tahun_pembuatan, warna)
        self.__jml_kursi = jml_kursi
        self.__jml_pintu = jml_pintu

    def display_info(self):
        """
        Menampilkan informasi kendaraan seperti plat nomor, merk, tahun pembuatan, warna,
        jumlah kursi, dan jumlah pintu.
        """
        super().display_info()
        print(f"Jumlah Kursi: {self.__jml_kursi}")
        print(f"Jumlah Pintu: {self.__jml_pintu}")

    def getJmlKursi(self):
        """
        Mendapatkan jumlah kursi dalam kendaraan.

        Returns:
        str: Jumlah kursi kendaraan.
        """
        return self.__jml_kursi
    
    def setJmlKursi(self, jml_kursi):
        """
        Mengatur jumlah kursi dalam kendaraan.

        Parameters:
        jml_kursi (str): Jumlah kursi kendaraan.
        """
        self.__jml_kursi = jml_kursi;

    def getJmlPintu(self):
        """
        Mendapatkan jumlah pintu dalam kendaraan.

        Returns:
        str: Jumlah pintu kendaraan.
        """
        return self.__jml_pintu
        
    def setJmlPintu(self, jml_pintu):
        """
        Mengatur jumlah pintu dalam kendaraan.

        Parameters:
        jml_pintu (str): Jumlah pintu kendaraan.
        """
        self.__jml_pintu = jml_pintu;
