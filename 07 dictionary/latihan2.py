print("======SISTEM MANAJEMEN TOKO BUKU======")
# program ini akan menyimpan data buku dalam bentuk list of tuple (judul, harga, stok)
# memungkinkan pengguna mencari buku berdasarkan judul
# menampilkan buku yang stok nya di bawah 5
# memproses pembelian dan mengupdate stok


# langkah pertama, membuat list untuk menyimpan data buku
buku = [
  ("Belajar Dasar Pemrograman", 150000, 10),
  ("Struktur Data Pemrograman", 170000, 3),
  ("Pemrograman Berbasis OOP", 160000, 5),
]

# langkah kedua, kita buat looping(perulangan) untuk menu utama
while True:
  print("\n===Edu Ono Niha Store===")
  print("1. Cari Buku")
  print("2. Cek Stok Rendah")
  print("3. Beli  Buku")
  print("4. Keluar")
  pilihan = input("Pilihan menu: ")

  #membuat kondisi jika ada pilihan menu
  # kondisi untuk menu 1
  if pilihan == "1" :
    cari = input("Masukkan judul buku: ").lower()
    ditemukan = False
    for item in buku: # loop melalui list buku
      if cari == item[0].lower():
        print(f"\n Judul : {item[0]}")
        print(f"\n Harga : Rp {item[1]: }")
        print(f"\n Stok : {item[2]}")
        ditemukan = True
    if not ditemukan:
      print("Buku tidak ditemukan!!")

  # kondisi untuk menu 2
  elif pilihan == "2" :
    print("\nBuku dengan stok rendah (<5):")
    for item in buku: # loop dan kondisi
      if item[2] < 5:
        print(f"-{item[0]} (Stok: {item[2]})")

  # Kondisi untuk menu 3
  elif pilihan == "3" :
    judul = input("Masukkan judul buku yang dibeli: ").lower()
    for i in range(len(buku)): # loop untuk cari indeks buku
      if judul == buku[i][0].lower():
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah > buku[i][2]:
          print("Stok tidak cukup!")
        else:
          # update stok (tuple tidak bisa diubah, jadi kita buat tuple baru)
          buku[i] = (buku[i][0], buku[i][1], buku[i][2] - jumlah)
          print(f"Berhasil membeli {jumlah} {buku[i][0]}!")
        break
    else:
      print("Buku tidak ditemukan")

  #kondisi untuk keluar
  elif pilihan == "4":
    print("Terimakasih")
    break
  else:
    print("pilihan tidak valid")