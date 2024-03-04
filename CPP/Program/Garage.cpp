#pragma once
#include <iostream>
#include <string>
#include <vector>

#include "Motorcycle.cpp"
#include "Car.cpp"

using namespace std;

// Garage class
class Garage
{
private:
    string nama_garasi;
    float luas_garasi;
    vector<Vehicle *> daftar_kendaraan;

public:
    Garage(string nama_garasi, float luas_garasi)
    {
        this->nama_garasi = nama_garasi;
        this->luas_garasi = luas_garasi;
    }

    void setNamaGarasi(string nama_garasi)
    {
        this->nama_garasi = nama_garasi;
    }

    void setLuasGarasi(float luas_garasi)
    {
        this->luas_garasi = luas_garasi;
    }

    string getNamaGarasi()
    {
        return nama_garasi;
    }

    float getLuasGarasi()
    {
        return luas_garasi;
    }

    void addVehicles(const vector<Vehicle *> &vehicles)
    {
        daftar_kendaraan.insert(daftar_kendaraan.end(), vehicles.begin(), vehicles.end());
    }

    void displayInfo()
    {
        cout << "Informasi garasi:" << endl;
        cout << "Nama Garasi: " << nama_garasi << endl;
        cout << "Luas Garasi: " << luas_garasi << " m2" << endl;
        cout << "Daftar Kendaraan:" << endl;
        cout << "---------------------" << endl;

        for (const auto &vehicle : daftar_kendaraan)
        {
            cout << "Plat Nomor: " << vehicle->getPlatNomor() << endl;
            cout << "Merk: " << vehicle->getMerk() << endl;
            cout << "Tahun Produksi: " << vehicle->getTahunProduksi() << endl;
            cout << "Warna: " << vehicle->getWarna() << endl;

            if (dynamic_cast<Car *>(vehicle) != nullptr)
            {
                Car *car = dynamic_cast<Car *>(vehicle);
                cout << "Jumlah Kursi: " << car->getJmlKursi() << endl;
                cout << "Jumlah Pintu: " << car->getJmlPintu() << endl;
            }
            else if (dynamic_cast<Motorcycle *>(vehicle) != nullptr)
            {
                Motorcycle *motorcycle = dynamic_cast<Motorcycle *>(vehicle);
                cout << "Jenis Motor: " << motorcycle->getTipeMotor() << endl;
                cout << "Kapasitas Tangki: " << motorcycle->getKapasitasTangki() << endl;
            }

            cout << "---------------------"<< endl;
        }

        cout << "\n";
    }

    ~Garage()
    {
        for (const auto &vehicle : daftar_kendaraan)
        {
            delete vehicle;
        }
    }
};