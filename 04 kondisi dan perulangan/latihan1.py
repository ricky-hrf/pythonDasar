print("=====MENENTUKAN BILANGAN PRIMA=====")
# Meminta input angka dari pengguna
angka = int(input("Masukkan angka: "))

if angka > 1:
    for i in range(2, angka):
        if angka % i == 0:
            print(f"{angka} BUKAN bilangan prima.")
            break
    else:
        print(f"{angka} adalah bilangan PRIMA.")
else:
    print(f"{angka} BUKAN bilangan prima.")

print("\n=====MEMBUAT DERET FIBONACI=====")
n = int(input("Masukkan jumlah angka Fibonaci: "))
#inisiasi dua angka pertama
a, b = 0, 1
print("deret fibonaci: ", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b