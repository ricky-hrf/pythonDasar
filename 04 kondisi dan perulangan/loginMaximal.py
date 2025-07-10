password = "admin"
for i in range(3):
    input_password = input("Masukkan password: ")
    if input_password == password:
        print("Login berhasil!")
        break
    else:
        print("Password salah, silakan coba lagi.")
print("Anda telah mencoba 3 kali, akses ditolak.")