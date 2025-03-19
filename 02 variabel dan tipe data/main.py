#variabel adalah tempat menyimpan data
print("ini adalah contoh dari penggunaan variabel")
a = 10 #variabel a menyimpan nilai 10
b = 5 #variabel b menyimpan nilai 5
c = a + b #variabel c menyimpan hasil penjumlahan variabel a dan b
print("a + b = ", c) #mencetak hasil penjumlahan
print("variabel dengan berbagai tipe data")
nama = "John Doe" #str
umur = 22 #int
tinggi = 170.5 #float
menikah = False #bool
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("menikah:", menikah)

#tipe data adalah jenis informasi yang disimpan dalam variabel, biasanya berisi value
#tipe data yang sering digunakan dalam python:
#str = string, berisi karakter/kalimat
print("tipe data string")
nama = "Tri"
print(nama)
print(type(nama))
#int = integer, berisi bilangan bulat
print("tipe data integer -> untuk bilagan bulat")
umur = 22
print(umur)
print(type(umur))
#float = floating point, berisi bilangan pecahan
print("tipe data float -> untuk bilangan pecahan")
tinggi = 170.5
print(tinggi)
print(type(tinggi))

#bool = boolean, berisi True atau False
print("tipe data boolean -> untuk menyatakan benar atau salah")
menikah = False
print(menikah)
print(type(menikah))

#list = kumpulan item yang terurut, bisa diubah
print("tipe data list")
buah = ["apel", "jeruk", "mangga"]
print(buah)
print(type(buah))

#tuple = kumpulan item yang terurut, tidak bisa diubah
print("tipe data tuple")
buah = ("apel", "jeruk", "mangga")
print(buah)
print(type(buah))

#set = kumpulan item yang tidak terurut, tidak bisa diindeks
print("tipe data set")
buah = {"apel", "jeruk", "mangga"}
print(buah)
print(type(buah))

#dict = kumpulan pasangan key dan value
print("tipe data dictionary")
siswa = {"nama": "Budi", "umur": 22}
print(siswa)
print(type(siswa))

