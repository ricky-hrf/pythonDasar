print("___PERULANGAN WHILE___")
angka = 0
while (angka < 10):
  print("Aku sudah berjalan sebanyak", angka, "langkah") 
  angka += 1

print("\n___CONTOH KEDUA___")
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment (menaikkan nilai i)

print("\n___CONTOH KETIGA___")
username = "admin"
password = "12345"
print("Masukkan username dan password untuk akses")
inputusername = input("Masukkan username: ")
inputpassword = input("Masukkan password: ")
while inputusername != "admin" and inputpassword != "12345":
    print("Username atau password salah. Silakan coba lagi.")
    inputusername = input("Masukkan username: ")
    inputpassword = input("Masukkan password: ")
print("Akses diberikan!")

print("___SEGITIGA BINTANG___")
tinggi = 5
baris = 0

while baris < tinggi:
    kolom = 0
    while kolom <= baris:
        print("*", end="")
        kolom += 1
    print()  # Pindah baris
    baris += 1

print("\n___SEGITIGA BINTANG TERBALIK___\n")
tinggi = 5
baris = tinggi

while baris > 0:
    kolom = 0
    while kolom < baris:
        print("*", end="")
        kolom += 1
    print()  # Pindah baris
    baris -= 1

print("\n___menghitung jumlah angka___\n")
angka = 1
jumlah = 0
while angka < 8:
    jumlah += angka
    print("Jumlah saat ini:", jumlah)
    angka += 1

print("\n___memunculkan angka genap___\n")
angka = 1
while angka < 8:
    if angka % 2 == 0:
        print("Angka genap:", angka)
    angka += 1

print("\n___memunculkan angka ganjil___\n")
angka = 1
while angka < 8:
    if angka % 2 != 0:
        print("Angka ganjil:", angka)
    angka += 1

print("\n==========Menghitung total bilangan genap==========\n")
angka = 1
total = 0
while angka < 8:
    if angka % 2 == 0:
        total += angka
    angka += 1
print("Total bilangan genap:", total)

print("\n==========Menghitung total bilangan ganjil==========\n")
angka = 1
total = 0
while angka < 8:
    if angka % 2 != 0:
        total += angka
    angka += 1
print("Total bilangan ganjil:", total)

print("\n=======PROGRAM MEMASUKKAN ANGKA SAMPAI NOL (0)=======\n")
angka = 1
while angka != 0:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
print("Program selesai. Anda memasukkan angka 0, keluar dari perulangan.")

print("\n=======PROGRAM MENGHITUNG JUMLAH ANGKA MASUKAN=======\n")
angka = 1
jumlah = 0
while angka != 0:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    jumlah += angka
print("Jumlah total angka yang dimasukkan:", jumlah)

print("\n=======PROGRAM MENEBAK ANGKA=======\n")
angka_rahasia = 9
angka_tebakan = int(input("Tebak angka (1-10): "))
while angka_tebakan != angka_rahasia:
    if angka_tebakan < angka_rahasia:
        print("Tebakan terlalu rendah. Coba lagi.")
    elif angka_tebakan > angka_rahasia:
        print("Tebakan terlalu tinggi. Coba lagi.")
    angka_tebakan = int(input("Tebak angka (1-10): "))
print("Selamat! Tebakan Anda benar.")

print("\n=======PROGRAM MENGHITUNG JUMLAH KARAKTER=======\n")
kalimat = input("Masukkan kalimat: ")
jumlah_karakter = 0
while jumlah_karakter < len(kalimat):
    jumlah_karakter += 1
print("Jumlah karakter:", jumlah_karakter)

print("\n=======PROGRAM MENGHITUNG JUMLAH VOKAL=======\n")
kalimat = input("Masukkan kalimat: ")
jumlah_vokal = 0
vokal = "aiueoAIUEO"
while jumlah_vokal < len(kalimat):
    if kalimat[jumlah_vokal] in vokal:
        print("Vokal ditemukan:", kalimat[jumlah_vokal])
    jumlah_vokal += 1

print("\n=======PROGRAM MENGHITUNG JUMLAH KONSONAN=======\n")
kalimat = input("Masukkan kalimat: ")
jumlah_konsonan = 0
konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
while jumlah_konsonan < len(kalimat):
    if kalimat[jumlah_konsonan] in konsonan:
        print("Konsonan ditemukan:", kalimat[jumlah_konsonan])
    jumlah_konsonan += 1

print("\n=======PROGRAM MEMBALIKKAN ANGKA=======\n")
angka = int(input("Masukkan angka: "))
angka_balik = 0
while angka > 0:
    digit = angka % 10
    angka_balik = angka_balik * 10 + digit
    angka //= 10
print("Angka setelah dibalik:", angka_balik)

print("\n=======PROGRAM MENGHITUNG FAKTORIAL=======\n")
angka = int(input("Masukkan angka untuk menghitung faktorial: "))
faktorial = 1
while angka > 0:
    faktorial *= angka
    angka -= 1
print("Faktorial:", faktorial)

print("\n=======PROGRAM MENGHITUNG DERET FIBONACCI=======\n")
angka = int(input("Masukkan jumlah deret Fibonacci: "))
fibonacci = [0, 1]
while len(fibonacci) < angka:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print("Deret Fibonacci:", fibonacci)

print("\n=======PROGRAM MENGHITUNG DERET ARITMATIKA=======\n")
angka = int(input("Masukkan jumlah suku deret aritmatika: "))
suku_awal = int(input("Masukkan suku awal: "))
selisih = int(input("Masukkan selisih: "))
deret_aritmatika = []
suku = suku_awal
while len(deret_aritmatika) < angka:
    deret_aritmatika.append(suku)
    suku += selisih
print("Deret Aritmatika:", deret_aritmatika)

print("\n=======PROGRAM MENGHITUNG DERET GEOMETRI=======\n")
angka = int(input("Masukkan jumlah suku deret geometri: "))
suku_awal = int(input("Masukkan suku awal: "))
rasio = int(input("Masukkan rasio: "))
deret_geometri = []
suku = suku_awal
while len(deret_geometri) < angka:
    deret_geometri.append(suku)
    suku *= rasio
print("Deret Geometri:", deret_geometri)

# membuat urutan angak 1 -20 dengan while dan angka 10 dilompati
angka = 1
while angka <= 20:
    if angka == 10:
        angka += 1
        continue  # Melewati angka 10
    print(angka)
    angka += 1