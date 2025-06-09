# program pengecekan tuple
print("========== Pengecekan Tuple ==========")
tuple_buah = ("apel", "jeruk", "mangga", "pisang")
buah = input("Masukkan nama buah: ")
if buah in tuple_buah:
    print(f"{buah} ada dalam tuple_buah")
else:
    print(f"{buah} tidak ada dalam tuple_buah")

print("========== Menampilkan angka menjadi huruf ==========")
tuple_angka_huruf = ("satu", "dua", "tiga", "empat", "lima")
tuple_angka = (1, 2, 3, 4, 5)
for angka in tuple_angka:
    print(angka,"=>", tuple_angka_huruf[angka - 1])
