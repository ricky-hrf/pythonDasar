print("======PROGRAM MENGHITUNG NILAI SUKU FIBONACI======")
def fibonacci(n):
    if n < 0:
        raise ValueError("n tidak boleh negatif")
    elif n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Masukkan nilai n: "))
print(f"F({n}) = {fibonacci(n)}")

print("======PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG======")
def hitung_luas_keliling(panjang, lebar):
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar harus positif")
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan lebar: "))
luas, keliling = hitung_luas_keliling(panjang, lebar)
print(f"Luas: {luas}, Keliling: {keliling}")

print("======PROGRAM MENGHITUNG RATA-RATA NILAI======")
def hitung_rata_rata(nilai_list):
    if not nilai_list:
        raise ValueError("List nilai tidak boleh kosong")
    total = sum(nilai_list)
    rata_rata = total / len(nilai_list)
    return rata_rata

nilai = [80, 90, 75, 85]
print(f"Rata-rata: {hitung_rata_rata(nilai)}")

print("======PROGRAM MENGHITUNG FAKTORIAL======")
def faktorial(n):
    if n < 0:
        raise ValueError("n tidak boleh negatif")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan nilai n: "))
print(f"Faktorial dari {n} adalah {faktorial(n)}")

print("======PROGRAM MENGHITUNG LUAS SEGITIGA======")
def hitung_luas_segitiga(alas, tinggi):
    if alas <= 0 or tinggi <= 0:
        raise ValueError("Alas dan tinggi harus positif")
    luas = 0.5 * alas * tinggi
    return luas

alas = int(input("Masukkan alas segitiga: "))
tinggi = int(input("Masukkan tinggi segitiga: "))
print(f"Luas segitiga: {hitung_luas_segitiga(alas, tinggi)}")
print("======PROGRAM MENGHITUNG LUAS BOLA======")
import math
def hitung_luas_bola(radius):
    if radius <= 0:
        raise ValueError("Radius harus positif")
    luas = 4 * math.pi * radius**2
    return luas

radius = int(input("Masukkan radius bola: "))
print(f"Luas bola: {hitung_luas_bola(radius)}")

print("======PROGRAM MENGHITUNG PERKALIAN DUA BILANGAN DENGAN REKURSIF======")
def kali(a, b):
    if b == 0:
        return 0
    else:
        return a + kali(a, b - 1)

x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
print(f"Hasil perkalian {x} * {y} = {kali(x, y)}")