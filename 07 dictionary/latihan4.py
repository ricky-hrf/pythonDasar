print("=====PROGRAM ANALISIS LIST ANGKA=====")
angka_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
angka_genap = []
angka_ganjil = []
for angka in angka_list:
    if angka % 2 == 0:
        angka_genap.append(angka)
    else:
        angka_ganjil.append(angka)
print("Angka genap:", angka_genap)
print("Angka ganjil:", angka_ganjil)

print("\n=====PROGRAM MENGHITUNG FREKUENSI KATA=====")
kalimat = "saya suka python dan saya suka coding"
kata = kalimat.split()
frekuensi = {}
for k in kata:
    frekuensi[k] = frekuensi.get(k, 0) + 1
for k, v in frekuensi.items():
    print(f"Kata '{k}' muncul sebanyak {v} kali.") 

print("\n=====DATABASE SEDERHANA=====")
students = {
    "001": {"nama": "ALICE", "nilai": 85},
    "002": {"nama": "BOB", "nilai": 95},
    "003": {"nama": "ADEL", "nilai": 90}
}
print("ID\tNama\tNilai")
for id, data in students.items():
    print(f"{id}\t{data['nama']}\t{data['nilai']}")

print("\n=====PROGRAM PENGHITUNG RATA-RATA NILAI=====")
total_nilai = sum(data['nilai'] for data in students.values())
rata_rata = total_nilai / len(students)
print(f"Rata-rata nilai: {rata_rata:.2f}")

print("\n=====PROGRAM PENCARIAN DATA MAHASISWA=====")
id_mahasiswa = input("Masukkan ID mahasiswa yang ingin dicari: ")
if id_mahasiswa in students:
    data = students[id_mahasiswa]
    print(f"ID: {id_mahasiswa}, Nama: {data['nama']}, Nilai: {data['nilai']}")
else:
    print("Data mahasiswa tidak ditemukan.")

print("\n=====PROGRAM PENAMBAHAN DATA MAHASISWA=====")
id_baru = input("Masukkan ID mahasiswa baru: ")
nama_baru = input("Masukkan nama mahasiswa baru: ")
nilai_baru = int(input("Masukkan nilai mahasiswa baru: "))
students[id_baru] = {"nama": nama_baru, "nilai": nilai_baru}
print("Data mahasiswa baru berhasil ditambahkan.")