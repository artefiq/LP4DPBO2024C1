class ParkingLot:
    def __init__(self, kapasitas, jml_kendaraan):
        """
        Inisialisasi objek ParkingLot dengan kapasitas dan jumlah kendaraan.

        Parameters:
        kapasitas (int): Kapasitas gedung parkir.
        jml_kendaraan (int): Jumlah kendaraan yang saat ini terparkir.
        """
        self.__kapasitas = kapasitas
        self.__jml_kendaraan = jml_kendaraan

    def add_vehicle(self, vehicle):
        """
        Menambahkan kendaraan ke dalam gedung parkir.

        Parameters:
        vehicle: Objek kendaraan yang akan ditambahkan.
        """
        self.__jml_kendaraan += 1

    def display_info(self):
        """
        Menampilkan informasi tentang gedung parkir, termasuk kapasitas dan jumlah kendaraan.
        """
        print(f"Kapasitas Gedung Parkir: {self.__kapasitas}")
        print(f"Jumlah Kendaraan: {self.__jml_kendaraan}")
