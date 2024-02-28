from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot

# garasi
garasiku = Garage("Garasi Depan", 5.25)

mobilku = Car("ABC123", "Toyota", 2022, "Merah", 5, 4)
motorku = Motorcycle("XYZ789", "Honda", 2020, "Biru", "Bebek", 10)

garasiku.add_vehicle(mobilku)
garasiku.add_vehicle(motorku)

garasiku.display_info()
print("-------------------------------\n\n")

# parking lot
parkiran = ParkingLot(100, 0)

parkiran.add_vehicle(mobilku)
parkiran.add_vehicle(motorku)

print("-------------------------------")
parkiran.display_info()
print("-------------------------------")