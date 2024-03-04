#pragma once
#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle
{
private:
    int jml_kursi;
    int jml_pintu;

public:
    Car() {}

    Car(string plat_nomor, string merk, int tahun_pembuatan, string warna, int jml_kursi, int jml_pintu)
        : Vehicle(plat_nomor, merk, tahun_pembuatan, warna), jml_kursi(jml_kursi), jml_pintu(jml_pintu) {}

    void setJmlKursi(int jml_kursi)
    {
        this->jml_kursi = jml_kursi;
    }

    void setJmlPintu(int jml_pintu)
    {
        this->jml_pintu = jml_pintu;
    }

    int getJmlKursi()
    {
        return jml_kursi;
    }

    int getJmlPintu()
    {
        return jml_pintu;
    }

    ~Car() {}
};
