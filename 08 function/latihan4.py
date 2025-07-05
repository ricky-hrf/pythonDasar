mahasiswa={}

def tambahData(data):
  while True:
    key = input("Input Key (quit untuk keluar): ").upper()
    if key == "QUIT":
      break
    valueType = input("Apakah type valuenya dictionary (y/n)?: ").lower()
    if valueType == "y":
      value = {}
      while True:
        keyDeep = input("Masukkan key (stop untuk keluar): ").upper()
        if keyDeep == "STOP":
          print("DATA BERHASIL DITAMBAHKAN KE DALAM DICTIONARY")
          break
        valueDeep = input(f"Input value untuk key {keyDeep}: ").capitalize()
        value[keyDeep] = valueDeep
        print(f"Data dengan key {keyDeep} Berhasil ditambahkan ke value")
    elif valueType == "n":
      value = input(f"Input value untuk key {key}: ").capitalize()
    else:
      print("pihan (y) atau (n) !!!")
    data[key]=value
  return data
# pemanggilan fungsi tambah data
tambahData(mahasiswa)

for keys, values in mahasiswa.items():
  print(keys, values)