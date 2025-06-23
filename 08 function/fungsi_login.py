print("======= FUNGSI LOGIN SEDERHANA =======")

def login(username, password, confirm):
    username_a = "admin"
    password_a = "123"
    if confirm == "1":
        print("anda keluar dari aplikasi")
    else:
        while username != username_a or password != password_a:
            print("username/password salah, silahkan coba lagi\n")
            username = input("masukkan username: ")
            password = input("Masukkan Password: ")
            confirm = input("yakin ingin masuk (ketik 1 untuk berhenti)?")
        print("SELAMAT DATANG DI APLIKASI PYTHON KAMI")
        
iusername = input("Masukkan username: ")
ipassword = input("Masukkan password: ")
iconfirm = input("yakin ingin masuk (ketik 1 untuk berhenti)?")
login(iusername, ipassword, iconfirm)