class Vehicle:
    def __init__(self, plat_nomor="", merk="", tahun_produksi="", warna=""):
        """
        Inisialisasi objek Vehicle dengan atribut-atributnya.

        Parameters:
        plat_nomor (str): Nomor plat kendaraan.
        merk (str): Merk kendaraan.
        tahun_produksi (str): Tahun produksi kendaraan.
        warna (str): Warna kendaraan.
        """
        self.__plat_nomor = plat_nomor
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    def display_info(self):
        """
        Menampilkan informasi kendaraan seperti plat nomor, merk, tahun produksi, dan warna.
        """
        print(f"Plat Nomor: {self.__plat_nomor}")
        print(f"Merk: {self.__merk}")
        print(f"Tahun Produksi: {self.__tahun_produksi}")
        print(f"Warna: {self.__warna}")

    def getPlatNomor(self):
        """
        Mendapatkan nomor plat kendaraan.

        Returns:
        str: Nomor plat kendaraan.
        """
        return self.__plat_nomor
    
    def setPlatNomor(self, plat_nomor):
        """
        Mengatur nomor plat kendaraan.

        Parameters:
        plat_nomor (str): Nomor plat kendaraan.
        """
        self.__plat_nomor = plat_nomor;

    def getMerk(self):
        """
        Mendapatkan merk kendaraan.

        Returns:
        str: Merk kendaraan.
        """
        return self.__merk
        
    def setMerk(self, merk):
        """
        Mengatur merk kendaraan.

        Parameters:
        merk (str): Merk kendaraan.
        """
        self.__merk = merk;

    def getTahunProduksi(self):
        """
        Mendapatkan tahun produksi kendaraan.

        Returns:
        str: Tahun produksi kendaraan.
        """
        return self.__tahun_produksi
        
    def setTahunProduksi(self, tahun_produksi):
        """
        Mengatur tahun produksi kendaraan.

        Parameters:
        tahun_produksi (str): Tahun produksi kendaraan.
        """
        self.__tahun_produksi = tahun_produksi;

    def getWarna(self):
        """
        Mendapatkan warna kendaraan.

        Returns:
        str: Warna kendaraan.
        """
        return self.__warna
    
    def setWarna(self, warna):
        """
        Mengatur warna kendaraan.

        Parameters:
        warna (str): Warna kendaraan.
        """
        self.__warna = warna;
