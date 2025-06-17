# membuat tuple yang berisi tuple lain
data_mahasiswa = (
  ("John", 20, 85),
  ("Alice", 22, 90),
  ("Bob", 21, 78)
)

# menghitung rata-rata nilai
total_nilai = sum(nilai for _, _, nilai in data_mahasiswa)
rata_rata = total_nilai/len(data_mahasiswa)
print("rata-rata nilai: ", rata_rata)

print("==== APLIKASI DATA BUKU ==== \n")
data_buku = (
  ("Buku A", "Pengarang A", 100),
  ("Buku B", "Pengarang B", 150),
  ("Buku C", "Pengarang C", 200)
)

for judul, pengarang, harga in data_buku:
    print(f"Judul: {judul}, Pengarang: {pengarang}, Harga: {harga}")