bilangan1 = int(input("Masukkan Bilangan Pertama: "))
bilangan2 = int(input("Masukkan Bilangan Kedua: "))
penjumlahan = bilangan1 + bilangan2
pengurangan = bilangan1 - bilangan2
perkalian = bilangan1 * bilangan2
pembagian = float(bilangan1 / bilangan2)
aksi = input("dihitung menggunakan apa? ").upper()
if aksi == "PENJUMLAHAN":
  hasil = penjumlahan
elif aksi == "PENGURANGAN":
  hasil = pengurangan
elif aksi == "PERKALIAN":
  hasil = perkalian
elif aksi == "PEMBAGIAN":
  hasil = pembagian
else:
  print("operator tidak valid! Harus penjumlahan, pengurangan, pembagian, perkalian")
  hasil = "tidak ada"
print(f"{bilangan1} + {bilangan2} = ", hasil)
