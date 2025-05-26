print("==========LATIHAN PERULANGAN WHILE===========")
angka = 1
while angka <= 5:
  print("Perulangan ke -", angka)
  angka += 1

print("==========MENAMPILKAN BELAJAR ITU SERU SEBANYAK 5 KALI===========")
ulang = 0
while ulang < 5:
  print("Belajar Python itu menyenangkan!")
  ulang += 1

print("==========keluar setelah menyerah===========")
nama = ""
while nama != "Out":
    nama = input("Masukkan nama (atau ketik 'Out'): ")

print("==========MENAMPILKAN ANGKA DARI 1-10===========")
bilangan = 1
while bilangan <= 10:
  print(bilangan)
  bilangan += 1

print("==========MENCETAK BILANGAN GENAP DARI 1 SAMPAI 20===========")
angka = 1
while angka <= 20:
  if angka % 2 == 0:
    print(angka, end=" ")
  angka += 1

print("\n==========MENCETAK BILANGAN GANJIL DARI 1 SAMPAI 20===========")
angka = 1
while angka <= 20:
  if angka % 2 == 1:
    print(angka, end=" ")
  angka += 1

print("\n==========MENCETAK BILANGAN KELIPATAN 5 SAMPAI 50===========")
angka = 5
while angka <= 50:
  print(angka, end=" ")
  angka += 5

print("\n==========MENCETAK BINTANG SEGITIGA===========")
angka = 1
while angka <= 5:
  print("*" * angka)
  angka += 1  
