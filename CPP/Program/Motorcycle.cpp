// Menggunakan pragma once agar header file hanya di-include satu kali
#pragma once
// Memasukan library yang digunakan, termasuk kelas induk (kelas Sivitas Akademik) dari kelas Dosen
#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Motorcycle : public Vehicle
{
private:
    string tipe_motor;
    float kapasitas_tangki;

public:
    Motorcycle() {}

    Motorcycle(string plat_nomor, string merk, int tahun_produksi, string warna, string tipe_motor, float kapasitas_tangki) : Vehicle(plat_nomor, merk, tahun_produksi, warna)
    {
        this->tipe_motor = tipe_motor;
        this->kapasitas_tangki = kapasitas_tangki;
    }

    void setTipeMotor(string tipe_motor)
    {
        this->tipe_motor = tipe_motor;
    }

    void setKapasitasTangki(float kapasitas_tangki)
    {
        this->kapasitas_tangki = kapasitas_tangki;
    }

    string getTipeMotor()
    {
        return tipe_motor;
    }

    float getKapasitasTangki()
    {
        return kapasitas_tangki;
    }

    ~Motorcycle() {}
};