#pragma once

#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
private:
    string plat_nomor;
    string merk;
    int tahun_produksi;
    string warna;

public:
    Vehicle() {}

    Vehicle(string plat_nomor, string merk, int tahun_produksi, string warna)
    {
        this->plat_nomor = plat_nomor;
        this->merk = merk;
        this->tahun_produksi = tahun_produksi;
        this->warna = warna;
    }

    void setPlatNomor(string plat_nomor)
    {
        this->plat_nomor = plat_nomor;
    }

    void setMerk(string merk)
    {
        this->merk = merk;
    }

    void setTahunProduksi(int tahun_produksi)
    {
        this->tahun_produksi = tahun_produksi;
    }

    void setWarna(string warna)
    {
        this->warna = warna;
    }

    string getPlatNomor() const
    {
        return plat_nomor;
    }

    string getMerk() const
    {
        return merk;
    }

    int getTahunProduksi() const
    {
        return tahun_produksi;
    }

    string getWarna() const
    {
        return warna;
    }

    virtual ~Vehicle() {}
};
