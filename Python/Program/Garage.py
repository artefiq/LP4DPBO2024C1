class Garage:
    def __init__(self, nama, luas):
        """
        Inisialisasi objek Garage dengan nama, luas, dan daftar kendaraan.

        Parameters:
        nama (str): Nama garasi.
        luas (float): Luas garasi dalam meter persegi.
        """
        self.__nama = nama
        self.__luas = luas
        self.__vehicle_list = []

    def add_vehicle(self, vehicle):
        """
        Menambahkan kendaraan ke dalam daftar kendaraan garasi.

        Parameters:
        vehicle: Objek kendaraan yang akan ditambahkan.
        """
        self.__vehicle_list.append(vehicle)

    def display_info(self):
        """
        Menampilkan informasi tentang garasi, termasuk nama, luas, dan daftar kendaraan.
        """
        print(f"Nama Garasi: {self.__nama}")
        print(f"Luas Garasi: {self.__luas} m2")
        print("Daftar Kendaraan:")
        for vehicle in self.__vehicle_list:
            print("-------------------------------")
            vehicle.display_info()
