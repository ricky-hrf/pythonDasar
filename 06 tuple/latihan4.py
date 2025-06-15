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