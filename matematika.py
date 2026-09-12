import os

def ganjil_genap():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("<========== Program untuk menentukan GANJIL/GENAP ==========>")
        
        try:
            angka = int(input("Masukkan bilangan yang akan diperiksa: "))
            if angka % 2 == 0:
                print(angka, "adalah bilangan genap 🟢")
            else:
                print(angka, "adalah bilangan ganjil 🔴")
        except ValueError:
            print("[ERROR] Masukkan angka bulat yang valid!")

        ulang = input("\nApakah ingin memeriksa bilangan lain? (Y/N): ").upper()
        if ulang != "Y":
            print("Terima kasih telah menggunakan program ini!")
            print("==================================================")
            break

def cek_prima():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("<========== Program untuk menentukan BILANGAN PRIMA ==========>")
        
        try:
            angka = int(input("Masukkan bilangan yang akan diperiksa: "))
            
            if angka < 2:
                print(angka, "bukan bilangan prima")
            else:
                prima = True
                for pembagi in range(2, int(angka ** 0.5) + 1):
                    if angka % pembagi == 0:
                        prima = False
                        break
                
                if prima:
                    print(angka, "adalah bilangan prima")
                else:
                    print(angka, "bukan bilangan prima")
                    
        except ValueError:
            print("[ERROR] Masukkan angka bulat yang valid!")

        ulang = input("\nApakah ingin memeriksa bilangan lain? (Y/N): ").upper()
        if ulang != "Y":
            print("Terima kasih telah menggunakan program ini!")
            break
    