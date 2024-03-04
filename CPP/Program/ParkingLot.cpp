#pragma once
#include <iostream>
#include <string>
#include <vector>

#include "Motorcycle.cpp"
#include "Car.cpp"

using namespace std;

class ParkingLot
{
private:
    int kapasitas;
    int jml_kendaraan;
    Motorcycle *motorcycle;
    Car *car;

public:
    ParkingLot() {}

    ParkingLot(int kapasitas, int jml_kendaraan)
    {
        this->kapasitas = kapasitas;
        this->jml_kendaraan = jml_kendaraan;
    }

    void setKapasitas(int kapasitas)
    {
        this->kapasitas = kapasitas;
    }

    void setJmlKendaraan(int jml_kendaraan)
    {
        this->jml_kendaraan = jml_kendaraan;
    }

    int getKapasitas()
    {
        return kapasitas;
    }

    int getJmlKendaraan()
    {
        return jml_kendaraan;
    }

    void addVehicle(const vector<Vehicle *> &vehicles)
    {
        int temp = 0;
        for (const auto &vehicle : vehicles)
        {
            temp++;
        }
        if (temp > jml_kendaraan)
        {
            jml_kendaraan = temp;
        }
    }

    void displayInfo()
    {
        cout << "Kapasitas Gedung Parkir: " << kapasitas << endl;
        cout << "Jumlah Kendaraan: " << jml_kendaraan << endl;
    }

    ~ParkingLot() {}
};
