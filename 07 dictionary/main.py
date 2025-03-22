print("Belajar dictionary")
#cara membuat dictionary itu dengan menggunakan kurung kurawal {}
mahasiswa = {
  "nama" : "Budi",
  "umur" : 20,
  "prodi" : "informatika"
}

#bisa juga menggunakan fungsi dict()
data = dict([("a", 1), ("b", 2)]) #datanya berupa list yang didalamnya diisi data tuple
# atau juga
data2 = dict(nama = "Andi", umur = 21)

# cara mengakses data di dalam dictionary 
print(f"Nama Mahasiswa: {mahasiswa['nama']}")
# misalkan di dalam dictionary kita tidak ada data yang ingin kita akses, kita bisa tambahkan nilai defaulnya
print(mahasiswa.get("alamat", "default"))

#jika mau menambahkan nilai
mahasiswa["ipk"] = 3.5 #menambahkan key baru ke dalam dictionary mahasiswa
print(mahasiswa)

#jika mau update nilai
mahasiswa["umur"] = 21
print(mahasiswa)

#menghapus elemen
del mahasiswa["umur"]
print(mahasiswa)
nilai = mahasiswa.pop("prodi")
print(mahasiswa)
