print("=====Program Tebak Angka=====")
#tentukan angka yang ingin ditebak
angka_rahasia = 7
tebakan = 0
print("Tebak angka antara 1 hingga 10!")
while tebakan != angka_rahasia:
    try:
        tebakan = int(input("Masukkan tebakanmu: "))
        
        if tebakan < angka_rahasia:
            print("Tebakan terlalu kecil! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Tebakan terlalu besar! Coba lagi.")
        else:
            print("Selamat! Tebakanmu benar")
    except ValueError:
        print("Masukkan angka yang valid!")
