# aplikasi menghitung nilai siswa
print("===PROGRAM MENGHITUNG NILAI SISWA===")
# list untuk data siswa
siswa = []
while True:
    nama = input("Masukkan nama siswa (ketik cukup untuk berhenti): ")
    if nama == "cukup":
        break
    nilai = float(input("Masukkan nilai siswa: "))
    siswa.append((nama, nilai))
print("Data Siswa:")
for nama, nilai in siswa:
    print("-", nama, ":", nilai)

print("===PROGRAM MENGHITUNG NILAI RATA-RATA===")
if len(siswa) > 0:
    total_nilai = sum(nilai for _, nilai in siswa)
    rata_rata = total_nilai / len(siswa)
    print("Nilai rata-rata siswa:", rata_rata)
else:
    print("Tidak ada data siswa.")

print("===PROGRAM MENENTUKAN STATUS LULUS===")
if rata_rata >= 75:
    status = "LULUS"
else:
    status = "TIDAK LULUS"
print("Status kelulusan siswa:", status)

print("===PROGRAM MENAMPILKAN DAFTAR SISWA===")
if len(siswa) > 0:
    print("Daftar siswa:")
    for nama, nilai in siswa:
        print("-", nama, ":", nilai)
else:
    print("Tidak ada data siswa.")

print("===PROGRAM MENCARI SISWA DENGAN NILAI TERTINGGI===")
if len(siswa) > 0:
    siswa_tertinggi = max(siswa, key=lambda x: x[1])
    print("Siswa dengan nilai tertinggi:")
    print("-", siswa_tertinggi[0], "dengan nilai:", siswa_tertinggi[1])
else:
    print("Tidak ada data siswa.")

print("===PROGRAM MENCARI SISWA DENGAN NILAI TERENDAH===")
if len(siswa) > 0:
    siswa_terendah = min(siswa, key=lambda x: x[1])
    print("Siswa dengan nilai terendah:")
    print("-", siswa_terendah[0], "dengan nilai:", siswa_terendah[1])
else:
    print("Tidak ada data siswa.")

print("===PROGRAM MENGHAPUS DATA SISWA===")
if len(siswa) > 0:
    nama_hapus = input("Masukkan nama siswa yang ingin dihapus: ")
    siswa = [s for s in siswa if s[0] != nama_hapus]
    print("Data siswa setelah penghapusan:")
    for nama, nilai in siswa:
        print("-", nama, ":", nilai)
else:
    print("Tidak ada data siswa untuk dihapus.")

print("===PROGRAM MENGHITUNG JUMLAH SISWA===")
jumlah_siswa = len(siswa)
print("Jumlah siswa:", jumlah_siswa)