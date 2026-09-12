import os
import sqlite3

DB_NAME = "app_user.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user():
    os.system("cls" if os.name == "nt" else "clear")
    print("========== BUAT AKUN BARU ==========")
    username = input("Masukkan Username Baru: ").strip()
    password = input("Masukkan Password Baru: ").strip()

    if not username or not password:
        print("\n[GAGAL] Username dan Password tidak boleh kosong!")
        input("\nTekan Enter untuk kembali...")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("\n[BERHASIL] Akun berhasil dibuat! Silakan login.")
    except sqlite3.IntegrityError:
        print("\n[GAGAL] Username sudah digunakan. Pilih username lain!")
    finally:
        conn.close()
    
    input("\nTekan Enter untuk kembali...")

def login_user():
    os.system("cls" if os.name == "nt" else "clear")
    print("========== LOGIN USER ==========")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return username
    else:
        return None

def auth_gate():
    init_db()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("========== AUTENTIKASI USER ==========")
        print("1. Login")
        print("2. Buat Akun Baru (Registrasi)")
        print("0. Keluar")
        print("=======================================")
        
        pilihan = input("Pilih menu (0-2): ")

        if pilihan == "1":
            username = login_user()
            if username:
                print(f"\n[SUKSES] Login berhasil!")
                return username
            else:
                print("\n[GAGAL] Username atau Password salah!")
                input("\nTekan Enter untuk mencoba lagi...")
        elif pilihan == "2":
            register_user()
        elif pilihan == "0":
            print("\nTerima kasih! Program dihentikan.")
            exit()
        else:
            print("\nPilihan tidak valid!")
            input("\nTekan Enter untuk mencoba lagi...")