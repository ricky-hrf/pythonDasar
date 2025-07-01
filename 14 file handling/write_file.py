# contoh1
def tulisData():
  file = open("file.txt", "w")
  file.write("ini adalah program python\n")
  file.close()
  print("Data telah ditulis ke dalam file.txt")
tulisData()

# contoh2
def tulisData2():
  file = open("news.txt", "w")
  print("Masukkan judul berita:")
  for i in range(3):
    isi = input("Masukkan isi berita:" + str(i + 1) + ": ")
    file.writelines(isi + "\n")
  file.close()
  print("proses penulisan file selesai")
  print("Isi file news.txt:", file.name)
tulisData2()