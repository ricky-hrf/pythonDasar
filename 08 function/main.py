#cara penulisan python
def sapa(nama):
  print(f"Hallo, {nama}! Selamat belajar pyhton!")

sapa("Budi")

#fungsi matematika
def tambah(angka1, angka2):
  return angka1 + angka2

hasil = tambah(10, 7)
print(hasil)

#fungsi dengan parameter default
def hitung_pajak(gaji, persen_pajak = 10):
  pajak = gaji * (persen_pajak/100)
  return gaji - pajak

gaji_bersih = hitung_pajak(5000000)
print(f"Gaji Bersih: Rp {gaji_bersih :,}")

gaji_bersih = hitung_pajak(5000000, 5)
print(f"Gaji Bersih: Rp {gaji_bersih:,}")

#fungsi rekursif
def faktorial(n):
  if n == 0:
    return 1
  else:
    return n * faktorial(n-1)
print(faktorial(5))

#fungsi dengan return multiple values
def hitung_luas_keliling(panjang, lebar):
  luas = panjang * lebar
  keliling = 2 * (panjang + lebar)
  return luas, keliling
luas, keliling = hitung_luas_keliling(8, 5)
print(f"Luas: {luas}, Keliling: {keliling}")