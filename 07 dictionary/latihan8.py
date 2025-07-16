# buat program yang menyimpan nama dan nilai siswa kemudian tampilkan siswa yang memiliki nilai lebih dari 75
siswa = {"Andi": 80, "Budi": 60, "cici": 90, "Doni": 70, "Eka": 85, "Fani": 50, "Gina": 95, "Hani": 65, "Ika": 75}
for nama, nilai in siswa.items():
    if nilai > 75:
        print(f" - {nama} memiliki nilai {nilai} yang lebih dari 75")

# Buat program yang menyimpan stok barang dalam dictionary. Jika pengguna membeli barang tertentu, stoknya dikurangi. Tampilkan stok setelah transaksi.
stok_barang = {
    "Pensil": 100,
    "Buku": 50,
    "Penghapus": 75 }

key_barang = input("Masukkan nama barang yang ingin dibeli: ")
jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))

if key_barang in stok_barang:
    stok_barang[key_barang] -= jumlah_beli
    if stok_barang[key_barang] < 0:
        print(f"Stok {key_barang} tidak mencukupi untuk jumlah yang diminta.")
        stok_barang[key_barang] += jumlah_beli  # kembalikan stok jika tidak mencukupi
    else:
        print(f"{jumlah_beli} {key_barang} berhasil dibeli. Stok sekarang: {stok_barang[key_barang]}")
else:
    print(f"{key_barang} tidak tersedia dalam stok.")
# stok akhir setelah transaksi
print("Stok akhir:", stok_barang)

# Diberikan sebuah kalimat, hitung berapa kali setiap kata muncul menggunakan dictionary
kalimat = "Python adalah bahasa pemrograman yang populer. Python mudah dipelajari dan banyak digunakan."
kata_count = {}
for kata in kalimat.split():
    kata = kata.strip(".").lower()
    kata_count[kata] = kata_count.get(kata, 0) + 1
print("Jumlah kemunculan setiap kata:")
for kata, count in kata_count.items():
    print(f"{kata}: {count}")

# Diberikan 2 dictionary barang dan jumlahnya, gabungkan jadi satu, dengan menjumlahkan nilai dari barang yang sama.
barang1 = {"Pensil": 10, "Buku": 5, "Penghapus": 8}
barang2 = {"Pensil": 5, "Buku": 3, "Penghapus": 2, "Spidol": 4}
gabungan_barang = {}
for barang in set(barang1) | set(barang2):
    gabungan_barang[barang] = barang1.get(barang, 0) + barang2.get(barang, 0)
print("Gabungan barang:")
for barang, jumlah in gabungan_barang.items():
    print(f"{barang}: {jumlah}")