import math

#data barang dengan harga satuan dan harga grosir
produk = {
  "Laptop" : (8000000, 7500000), # harga normal, harga grosir
  "Mouse" : (150000, 250000), # harga normal, harga grosir
  "Keyboard" : (300000, 250000), # harga normal, harga grosir
  "Monitor" : (2000000, 1800000), # harga normal, harga grosir
  "Flashdisk" : (100000, 80000), # harga normal, harga grosir
}

#buat fungsi untuk menghitung harga berdasarkan jumlah
def hitung_harga(nama_barang, jumlah):
  if nama_barang in produk:
    harga_satuan, harga_grosir = produk[nama_barang]
    if jumlah >= 3:
      return jumlah * harga_grosir 
    else:
      return jumlah * harga_satuan
  else:
    return 0
  
# fungsi untuk menghitung total belanja dan diskon
def hitung_total(belanja):
  total = 0
  for barang, jumlah in belanja.items():
    total += hitung_harga(barang, jumlah)

    #diskon 10% jika total belanja lebih dari 200.000
    diskon = 0
    if total > 200000:
      diskon = total * 0.1
      total -= diskon
      
    return total, diskon
  
#list untuk menyimpan data yang dibeli
keranjang = {}

# looping untuk input belanjaan 
while True:
  barang = input("Masukan nama barang (atau 'selesai' untuk checkout): ").title()
  if barang.lower() == "selesai":
    break
  if barang not in produk:
    print("Barang tidak tersedia!")
    continue

  jumlah = int(input(f"Masukan jumlah {barang}: "))

  # simpan ke keranjang belanja
  if barang in keranjang:
    keranjang[barang] += jumlah
  else:
    keranjang[barang] =jumlah

# hitung total harga dan diskon
total_bayar, diskon_diberikan = hitung_total(keranjang)

# output
print("==== STRUK BELANJA ===")
for barang, jumlah in keranjang.items():
  harga_total = hitung_harga(barang, jumlah)
  print(f"{barang} ({jumlah}x) - Rp{harga_total:,}")

print(f"Diskon: Rp{diskon_diberikan:,}")
print(f"Total yang harus dibayar: Rp{total_bayar:,}")
print("======================")
