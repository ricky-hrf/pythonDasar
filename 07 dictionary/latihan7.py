barang ={
  "B001":{
    "tv": "television",
    "cs": "Kulkas",
    "hp": "Handphone"
  },
  "B002":"Ikat Rambut",
  "B003":"Loudspeaker",
  "B004":"Meja Belajar",
  "B005":"Gelas Kaca"
}
# print(type(barang))
# print(barang.keys())
# print(barang.values())
# for kunci in barang.keys():
#   print(kunci)
# for isi in barang.values():
#   print(isi)
# for kunci, isi in barang.items():
# #   print(kunci,":",isi)
print("APLIKASI MENCARI ISI DALAM DICTIONARI")
inputan=input("ketikkan kode barang yang ingin dicari namanya: ").upper()
defenisi = barang.get(inputan)
if defenisi:
    if type(defenisi)=="dict":
      for key, isi in defenisi.items():
        print(key, isi)
    else:    
      print(defenisi)
else:
  print("barang tidak ada dalam daftar")