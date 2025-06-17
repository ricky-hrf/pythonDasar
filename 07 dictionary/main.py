print("Belajar dictionary")
#cara membuat dictionary itu dengan menggunakan kurung kurawal {}
mahasiswa = {
  "nama" : "Tri",
  "umur" : 20,
  "prodi" : "informatika"
}

#bisa juga menggunakan fungsi dict()
data = dict([("a", 1), ("b", 2)]) #datanya berupa list yang didalamnya diisi data tuple
# atau juga
data2 = dict(nama = "Andi", umur = 21)

# cara mengakses data di dalam dictionary 
print(f"Nama Mahasiswa: {mahasiswa['nama']}")
# misalkan di dalam dictionary kita tidak ada data yang ingin kita akses, kita bisa tambahkan nilai defaultnya
print(mahasiswa.get("alamat", "default"))

#jika mau menambahkan nilai
mahasiswa["ipk"] = 3.5 #menambahkan key baru ke dalam dictionary mahasiswa
print(mahasiswa)

#jika mau update nilai
mahasiswa["umur"] = 21
print(mahasiswa)

mahasiswa["ipk"] = 3.8 #update nilai ipk
print(mahasiswa)

#menghapus elemen menggunakan del
del mahasiswa["umur"]
print(mahasiswa)

#atau bisa juga menggunakan fungsi pop()
nilai = mahasiswa.pop("prodi")
print(mahasiswa)
print(f"Nilai yang dihapus: {nilai}")

#atau bisa juga menggunakan fungsi popitem() untuk menghapus elemen terakhir
nilai_terakhir = mahasiswa.popitem()
print(f"Nilai yang dihapus: {nilai_terakhir}")

#atau bisa juga menggunakan fungsi clear() untuk menghapus semua elemen
mahasiswa.clear()
print(f"Data mahasiswa setelah dihapus: {mahasiswa}")

#atau bisa juga menggunakan fungsi keys() untuk mengambil semua key
keys = mahasiswa.keys()
print(f"Semua key: {keys}")

