print("========== TUGAS NOMOR 1 ==========")
d= {
  1:10,
  2:20,
  3:30,
  4:40
}
print(d)
print(type(d))
print(d.keys())

print("========== TUGAS NOMOR 2 ==========")
hewan = {
  "lucky":"Dog",
  "chick":"Ayam",
  "aung":"tiger"
}
key_hewan = hewan.keys()
print(key_hewan)
value_hewan = hewan.values()
print(value_hewan)
for key_hewan, value_hewan in hewan.items():
  print(f"{key_hewan} is a {value_hewan}")