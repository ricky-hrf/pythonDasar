print("===PROGRAM MENGHITUNG NILAI SISWA===")

#list untuk data siswa
siswa = []

#inputan untuk menerima data siswa
print("Masukkan data siswa  (ketik 'selesai' untuk nama jika ingin berhenti..!!) : ")
while True :
  nama = input("\nNama Siswa : ")
  if nama.lower() == "selesai":
    break

  #input nilai
  nilai_input = input("Masukkan nilai (pisahkan spasi): ")
  try:
    nilai_list = list(map(int, nilai_input.split()))
  except ValueError:
    print("Error: Input harus angka, silahkan ulangi")
    continue
  siswa.append((nama, nilai_list))

  laporan = []
  #proses perhitungan menggunakan for (perulangan)
  for student in siswa:
    nama, nilai = student
    rata_rata = sum(nilai)/len(nilai)
    
    #tentukan status menggunakan if (kondisi)
    if rata_rata >= 75:
      status = "LULUS"
    else:
      status = "TIDAK LULUS"

    laporan.append((nama, round(rata_rata, 2), status))

#tampilkan ke layar
print("\n=== Laporan Hasil ===")
print("{:<15} {:<10} {:<10}".format("Nama", "Rata-Rata", "Status"))
for data in laporan:
    print("{:<15} {:<10} {:<10}".format(data[0], data[1], data[2]))