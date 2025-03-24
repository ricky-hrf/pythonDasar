def hitung_pajak(harga, persen_pajak):
  return harga*(persen_pajak / 100)

def total_harga(harga, persen_pajak):
  pajak = hitung_pajak(harga, persen_pajak)
  return harga + pajak

#contoh penggunaan
harga_barang = 100000
pajak_barang = 10 #10%

total = int(total_harga(harga_barang, pajak_barang))
print(f"Total harga termasuk pajak: Rp{total}")