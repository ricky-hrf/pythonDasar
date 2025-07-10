print("======= FUNGSI LOGIN SEDERHANA =======")

def login(username, password, confirm):
    username_a = "admin"
    password_a = "123"
    if confirm == "1":
        print("anda keluar dari aplikasi")
    else:
        for i in range(3):
            if username == username_a and password == password_a:
                print("Login berhasil!")
                print("SELAMAT DATANG DI APLIKASI PYTHON KAMI")
                break
            else:
                print("username/password salah, silahkan coba lagi")
                username = input("masukkan username: ")
                password = input("Masukkan Password: ")
                confirm = input("yakin ingin masuk (ketik 1 untuk berhenti)?")
        
iusername = input("Masukkan username: ")
ipassword = input("Masukkan password: ")
iconfirm = input("yakin ingin masuk (ketik 1 untuk berhenti)?")
login(iusername, ipassword, iconfirm)