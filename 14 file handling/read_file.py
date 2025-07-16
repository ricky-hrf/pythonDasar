# membaca sebuah file dan menampilkan isinya
# def bacafile():
#   fileQ = open("file.txt", "r")
#   isiFile = fileQ.read()
#   fileQ.close()

#   print("Isi file.txt:")
#   print(isiFile)

# bacafile()

# membaca sebuah file dan menampilkan isinya per baris
def bacafile():
  fileQ = open("file.txt", "r")
  baris_1 = fileQ.readline()
  baris_2 = fileQ.readline()
  fileQ.close()

  print("Isi file.txt:")
  print(baris_1)
  print(baris_2)

bacafile()
