# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:28:09 2024

@author: Rangga Aditya
"""

print("Nama : Rangga Aditya Pradana")
print("NIM : 064002300026")
print("PROGRAM MENGHITUNG KELILING & LUAS SEGITIGA")

class Segitiga:
    def hitung_keliling(self, sisi1, sisi2, sisi3):
        return sisi1 + sisi2 + sisi3

    def hitung_luas(self, alas, tinggi):
        return 0.5 * alas * tinggi

print("1. Keliling")
print("2. Luas")

pilihan = int(input("Masukan pilihan: "))
segitiga = Segitiga()

if pilihan == 1:
    sisi1 = float(input("Masukan panjang sisi 1: "))
    sisi2 = float(input("Masukan panjang sisi 2: "))
    sisi3 = float(input("Masukan panjang sisi 3: "))
    keliling = segitiga.hitung_keliling(sisi1, sisi2, sisi3)
    print("Keliling Segitiga:", keliling, "cm")
elif pilihan == 2:
    alas = float(input("Masukan panjang alas: "))
    tinggi = float(input("Masukan tinggi: "))
    luas = segitiga.hitung_luas(alas, tinggi)
    print("Luas Segitiga:", luas, "cm^2")
else:
    print("Pilihan tidak valid.")

print("Terima kasih")


