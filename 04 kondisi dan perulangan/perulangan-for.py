#perulangan for, digunakan untuk mengulang elemen dalam list
print("=====PERULANGAN FOR=====")
for i in range(1, 10):
  print ("ini perulangan ke -", i)

buah = ["\napel", "mangga", "jeruk"]
for item in buah:
  print(item)

  for huruf in "\nSUMATERA COMPUTER CENTRE":
    print(huruf)

print("===Mencetak angka ganjil===")
for angka in range(1, 16, 2):
  print(angka, end = " ")

print("===MENCETAK ANGKA MUNDUR===")
for angka in range(10, 0, -1):
  print(angka, end="")

print("===menghitung total===")
total = 0
for angka in range (1, 11):
  total += angka
  print("Total: ", total)

  print("___SEGITIGA BINTANG___")
  for a in range(1, 6):  
    print("*" * a)
