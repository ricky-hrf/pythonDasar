import os
os.system('cls' if os.name == 'nt' else 'clear')

DataBarang = (("Beras", 10000), ("Gula", 12000), ("Minyak Goreng", 15000))
searchProduk = input("Masukkan nama produk yang ingin dicari: ")
# found = False
for barang, harga in DataBarang:
    if searchProduk.lower() == barang.lower():
        print(f"Barang: {barang}, Harga: {harga:,}".replace(',', '.'))
        break
        # found = True
# if not found:
else:
    print(f"Produk {searchProduk} tidak ditemukan.")