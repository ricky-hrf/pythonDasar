print("==========MENAMPILKAN TULISAN SELAMA 5 KALI===========")
for i in range(5):
    print("Belajar Python itu menyenangkan!")

print("==========MENAMPILKAN ANGKA 1 - 10===========")
for i in range(1, 11):
    print(i)

print("==========MENCETAK BILANGAN KELIPATAN 3 SAMPAI 30===========")
for i in range(3, 31, 3):
    print(i)

print("==========HITUNG JUMLAH ANGKA DARI 1 SAMPAI 5===========")
jumlah = 0
for i in range(1, 6):
    jumlah += i
print("Jumlah dari 1 sampai 5 adalah:", jumlah)

print("==========MENCETAK BINTANG SEGITIGA===========")
for i in range(1, 6):
    print("*" * i)

print("==========MENCETAK HASIL INPUTAN===========")
text = input("Masukkan teks yang ingin dicetak: ")
for huruf in text:
    print(huruf)

# print("==========LATIHAN PERULANGAN FOR===========")
# for i in range(1, 11):
#     print("Perulangan ke -", i)
#     if i % 2 == 0:
#         print(i, "adalah bilangan genap")
#     else:
#         print(i, "adalah bilangan ganjil")
# print("===MENCETAK BILANGAN GENAP DARI 1 SAMPAI 20===")
# for angka in range(1, 21):
#     if angka % 2 == 0:
#         print(angka, end=" ")
