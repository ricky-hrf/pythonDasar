print("====== METHOD DICTIONARY ======")
data_siswa = {
  "S07A" : "Vania Wijaya",
  "S08B" : "Heru Dermawan",
  "S09A" : "Siska Avengelist",
  "S07B" : "Bayu Gerand",
  "S08A" : "Adel Naziya"
}
data = len(data_siswa)
print(data)

# menambahkan data ke dalam dictionary dengan menerima inputan
while True:
  key = input("Masukkan key: ").upper()
  if key == "STOP":
    break
  value = input(f"Masukkan value untuk key {key}: ").capitalize()
  data_siswa.update({key:value})
  print(f"data dengan key {key} berhasil ditambahkan")
for keys, values in data_siswa.items():
  print(f"{keys}:{values}")

