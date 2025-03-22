print("=====MENGHITUNG FREKUENSI KATA=====")
kalimat = "saya suka python dan saya suka coding"
kata = kalimat.split()
frekuensi = {}

for k in kata:
  frekuensi[k] = frekuensi.get(k, 0) + 1

  print(frekuensi)

print("======DATABASE SEDERHANA======")
students = {
  "001" : {"nama": "ALICE", "nilai": 85},
  "002" : {"nama": "BOB", "nilai": 95},
  "003" : {"nama": "ADEL", "nilai": 90}
}

#kita akses datanya, misalkan data adel
print(students["003"]["nama"])
