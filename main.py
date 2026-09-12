# File: main.py
import os
import bangun_datar as bd
import matematika as mt
import auth as au

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("========== PROGRAM UTAMA ==========")
    print("1. Hitung Luas Persegi Panjang")
    print("2. Cek Bilangan Ganjil/Genap")
    print("3. Cek Bilangan Prima")
    print("0. Keluar")
    print("===================================")

# ------- WAJIB LOGIN SEBELUM MASUK PROGRAM -------
os.system("cls" if os.name == "nt" else "clear")
username_aktif = au.auth_gate()

print(f"\nAnda login sebagai: {username_aktif}")
input("\nTekan Enter untuk melanjutkan ke program utama...")

while True:
    menu()
    pilihan = input("Pilih menu (0-3): ")

    if pilihan == "1":
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = bd.hitung_luas_persegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang adalah: {luas}")
        input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "2":
        mt.ganjil_genap()

    elif pilihan == "3":
        mt.cek_prima()

    elif pilihan == "0":
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk mencoba lagi...")