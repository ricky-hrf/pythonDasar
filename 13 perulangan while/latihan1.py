print("========== APLIKASI MENCETAK ANGKA DARI 1 -10 ==========")
angka = 1
while angka <= 10:
  print("Ini angka ke", angka)
  angka += 1

print("\n========== APLIKASI MENGHITUNG JUMLAH BILANGAN GENAP DARI 1 - 100 ==========")
bilangan = 1
jumlah = 0
while bilangan <= 100:
  if bilangan % 2 == 0:
    print(f"Menambahkan {bilangan} ke jumlah saat ini ({jumlah})")
    jumlah += bilangan
    print(f"jumlah sekarang: {jumlah}\n")
  bilangan += 1
print(f"Jumlah bilangan genap dari 1 sampai 100 adalah: {jumlah}")