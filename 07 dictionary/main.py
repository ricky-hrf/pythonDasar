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

# update menggunakan method update()
mahasiswa.update({"nama": "Budi", "umur": 22})

# update keys
mahasiswa.update(nama="Siti", prodi="Sistem Informasi")
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

# menggunakan method value
values = mahasiswa.values()
print("Semuan values", values)

data_lagu = {
  "pop": {
    "judul": "Bongkar",
    "vokalis":"iwan fals"
    },
  "jazz": {
    "judul": "kurang tau bang",
    "vakalis": "orang lah, gak mungkin batu"
  }
}

kunci_dict = data_lagu.keys()
isi_dict = data_lagu.values()
print(kunci_dict)
print(isi_dict)
print(data_lagu["jazz"]["judul"])
print(data_lagu["pop"])

for kunci in data_lagu.keys():
  print(kunci)

for isi in data_lagu.values():
  print(isi)

for kunci, isi in data_lagu.items():
  print(f"{kunci}:{isi}")

# contoh penggunaan fungsi del di dict
del data_lagu["pop"]
print(data_lagu)