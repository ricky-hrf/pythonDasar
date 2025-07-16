# print("=====LATIHAN MENGECEK BILANGAN NEGATIF ATAU POSITIF=====")
# x = int(input("Masukkan angka: "))
# if x > 0:
#   print(x, "merupakan bilangan positif!")
# else:
#   print(x, "adalah bilangan negatif")

# print("=====LATIHAN MENGECEK BILANGAN GANJIL ATAU GENAP=====")
# if x%2 == 0:
#   print(x, "Bilangan Genap")
# elif x % 2 == 1:
#   print(x, "Bilangan Ganjil")
# else:
#   print(x, "tidak bisa ditebak")

# print("=====LATIHAN MENGECEK BILANGAN GANJIL ATAU GENAP=====")
# if x >= 85:
#   print("nilai yang andan masukkan adalah: ", x, "hasilnya A")
# elif x >= 70:
#   print("nilai yang andan masukkan adalah: ", x, "hasilnya B")
# elif x >= 60:
#   print("nilai yang andan masukkan adalah: ", x, "hasilnya C")
# elif x < 60:
#   print("nilai yang andan masukkan adalah: ", x, "hasilnya D")
# else:
#   print("Tidak bisa ditebak")
'''print("======Aplikasi Mengecek Tahun Kabisat atau Tidak===========")
tahun = int(input("Masukkan tahun yang ingin anda caritau: cth:2024...."))
if (tahun % 400 ==0) or (tahun % 100 != 0 and tahun % 4 == 0) :
  print(tahun, "Adalah tahun kabisat")
else:
  print(tahun, "Adalah tahun biasa")
'''
# print("=====LATIHAN MENGECEK BILANGAN PRIMA=====")
n = int(input("Masukkan bilangan: "))
if n > 1:
  if n == 2:
    print(n, "adalah bilangan prima")
  elif n % 2 == 0:
    print(n, "bukan bilangan prima")
  else:
    print(n, "adalah bilangan prima")
