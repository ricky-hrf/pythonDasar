print("perulangan dengan nested")
for i in range(3):  
    for j in range(3):  
        print(f"i={i}, j={j}")

for i in range(1, 6):  
    for j in range(i):  
        print("*", end="")  
    print() 

    for a in range(1, 6):  
        for b in range(1, 6):  
            print(a * b, end="\t") 
    print() 

    jam = 1

while jam <= 2:  
    menit = 0
    while menit < 60:  
        print(f"Jam {jam}, Menit {menit}")
        menit += 30  
    jam += 1

print("\n===Perulangan Buah===")
buah = {
    "Medan": ["apel", "mangga", "jeruk"],
    "Jakarta": ["pisang", "durian", "nanas"],
    "Surabaya": ["anggur", "semangka", "kiwi"]
}

for kota, daftar_buah in buah.items():
    print(f"Buah-buahan di {kota}:")
    for nama_buah in daftar_buah:
        print(f" - {nama_buah}")

print("\n===Perulangan dengan konsep jam===")
for jam in range(1,6):
    print(f"Jam ke-{jam}")
    for menit in range(0, 15):
        print(f" - Menit ke-{menit}")

print("\n===Perulangan dengan konsep angka===")
angka = [1, 2, 3, 4, 5]
for i in angka:
    for j in angka:
        print(f"{i} x {j} = {i * j}")
    print()

print("\n===Perulangan dengan konsep angka terbalik===")
angka = [5, 4, 3, 2, 1]
for i in angka:
    for j in angka:
        print(f"{i} x {j} = {i * j}")
    print()

print("\n===Perulangan dengan konsep segitiga rata kiri===")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\n===Perulangan dengan konsep segitiga rata kanan===")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

print("\n===Perulangan dengan konsep segitiga piramida===\n")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i-1):
        print("*", end="")
    print()

print("\n===Perulangan dengan konsep segitiga piramida terbalik===\n")
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

print("\n===Perulangan dengan konsep belah ketupat===\n")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))

print("\n===Perulangan dengan konsep segitiga ganjil naik===\n")
for i in range(1, 9, 2):
    for j in range(i):
        print("*", end="")
    print()

print("\n===Perulangan dengan konsep segitiga genap turun===\n")
for i in range(9, 0, -2):
    for j in range(i):
        print("*", end="")
    print()

print("\n===Perulangan dengan konsep piramida kosong===\n")
n = 5 
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    if i == 1:
        print("*")
    elif i == n:
        for k in range(2 * n - 1):
            print("*", end="")
        print()
    else:
        print("*", end="") 
        for j in range(2 * i - 3): 
            print(" ", end="")
        print("*")
