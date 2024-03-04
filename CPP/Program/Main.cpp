#include <bits/stdc++.h>

#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"
#include "ParkingLot.cpp"

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie();

    Car mobilku("ABC123", "Toyota", 2022, "Merah", 5, 4);
    Motorcycle motorku("XYZ789", "Honda", 2020, "Biru", "Bebek", 10);

    vector<Vehicle *> vehicles;
    vehicles.push_back(&mobilku);
    vehicles.push_back(&motorku);

        Garage garage("Garasi Depan", 5.25);
    garage.addVehicles(vehicles);
    garage.displayInfo();

    ParkingLot parkiran(100, 0);
    parkiran.addVehicle(vehicles);
    parkiran.displayInfo();

    for (const auto &vehicle : vehicles)
    {
        delete vehicle;
    }

    return 0;
}