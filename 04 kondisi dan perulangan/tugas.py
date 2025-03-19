print("====Tugas====")

nama = input("Nama Pegawai: ")
Golongan = input("Golongan Pegawai (A/B/C): ").upper()
GajiPokok = float(input("Masukkan Gaji:"))

if Golongan == "A":
  bonus = GajiPokok*0.20
elif Golongan == "B":
  bonus = GajiPokok*0.15
elif Golongan == "C":
  bonus = GajiPokok*0.10
else:
  print("Golongan tidak valid! Harus A, B, atau C")
  bonus = 0

print("====Hasil Perhitungan Gaji Karyawan====")
print(f"Nama : {nama}")
print(f"Golongan : {Golongan}")
print(f"Gaji Pokok : Rp {GajiPokok:,.2f}")
print(f"Bonus : Rp {bonus:,.2f}")
print(f"Total Gaji : Rp {GajiPokok + bonus:,.2f}")

print("___PROGRAM FAKTOR PERKALIAN___")
#input angka dari keyboard
angka = int(input("Masukkan angka: "))
#loop untuk menghasilkan faktor
print(f"Faktor dari {angka}: ", end="")
for i in range(1, angka + 1):
  if angka % i == 0:
    print(i, end=" ")

print("\n___PROGRAM INPUT NAMA___")
#buat tampungan untuk nama anda
name = ""
#lakukan pengecekan pada inputan terhadap nama anda
while name != "Tri":
  name = input("Masukkan Nama Anda: ")
print(f"Oke, selamat datang {name}")

print("\n===Menentukan Bilangan Ganjil atau Genap===")
#terima inputan dari user
bilangan = int(input("Masukkan Bilangan yang ingin anda cek: "))
#masukkan kondisi bila inputan sudah diterima
if bilangan % 2 == 0 :
  print(f"Bilangan {bilangan} adalah Bilangan GENAP")
else:
  print(f"Bilangan {bilangan} adalah Bilangan GANJIL")