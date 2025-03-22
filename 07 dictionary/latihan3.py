print("=====APLIKASI PEMESANAN MAKANAN=====")
# menyimpan menu di dalam tuple
menu = (
  ("A1", "Nasi Goreng", 15000),
  ("A2", "Mie Ayam", 12000),
  ("A3", "Teh Manis", 5000)
)

# langkah kedua, kita buatkan list untuk menyimpan pesanan
pesanan = []

# langkah ketiga, kita lakukan loop untuk aktifitas pemesanan
while True:
  print("\n === Menu Kedai ===") # kita cetak judul tampilan menu
  for item in menu: # kita loop lagi untuk menu awal
    print(f"{item[0]}. {item[1]} - Rp {item[2]:,}")
  kode = input("\n Masukkan kode menu (atau 'selesai'): ").upper()

  #kondisi untuk berhenti
  if kode == "SELESAI" :
    break

  #langkah keempat, kita cari item di menu
  ditemukan = False # awalnya kosong
  for item in menu:
    if kode == item[0]:
      jumlah = int(input("Masukkan jumlah Pesanan: "))
      pesanan.append((item[0], jumlah, item[2])) # menambahkan ke list pesanan ke list yang kosong pada awal kita mulai coding
      print(f"{item[1]} x {jumlah} ditambahkan!")
      ditemukan = True
      break
  if not ditemukan:
    print("Kode tidak valid")

#langkah terakhir kita hitung total dan tampilan laporan pesanan kita
total = 0 # awalnya totalnya 0
print("=====STRUK PEMBAYARAN=====")
for p in pesanan: # kita loop hitung total
  subtotal = p[1] * p[2]
  print(f"{p[0]} x  {p[1]} : Rp {subtotal:,}")
  total += subtotal

  print(f"Total : Rp {total:,}")